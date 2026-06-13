"""
match_scheduler.py
==================
Builds a season match schedule from a per-week division map.

Design (confirmed with the requester):
  * Each team plays EXACTLY `matches_per_week` matches every week.
  * The roster is constant across the season; only divisions change week to week.
  * A "match" is an unordered pair of teams. Uniqueness is tracked GLOBALLY across
    the whole season and is independent of any division changes.
  * Objective priority (lexicographic):
        1. Maximize the number of distinct matchups played over the season.
           (Because total match count is fixed by the exact-k rule, this is
            mathematically identical to minimizing duplicates.)
        2. Among all max-unique solutions, maximize division affinity, where a
           match scores: same division = 2, "nearby" = 1, "far" = 0.
        3. Separately, assign home/away to balance each team's home vs away count
           and to flip the orientation of any pair that must be played twice.
  * Division "nearness": two divisions are the SAME if they cover the same set of
    base regions (so "East/Central" == "Central/East"); they are NEARBY if their
    region sets overlap (e.g. East and East/Central); otherwise they are FAR.

Requires: ortools  (pip install ortools)
"""

from __future__ import annotations

import csv
from collections import defaultdict
from itertools import combinations
from typing import Dict, List, Tuple

from ortools.sat.python import cp_model


# --------------------------------------------------------------------------- #
# Division helpers
# --------------------------------------------------------------------------- #
def regions_of(division: str) -> frozenset:
    """Split a division label into its base regions: 'East/Central' -> {East, Central}."""
    return frozenset(part.strip() for part in division.split("/") if part.strip())


def division_tier(div_a: str, div_b: str) -> str:
    """Return 'intra', 'nearby', or 'far' for two division labels."""
    ra, rb = regions_of(div_a), regions_of(div_b)
    if ra == rb:
        return "intra"
    if ra & rb:
        return "nearby"
    return "far"


TIER_SCORE = {"intra": 2, "nearby": 1, "far": 0}


# --------------------------------------------------------------------------- #
# Round-robin warm start
# --------------------------------------------------------------------------- #
def _round_robin_rounds(m: int) -> List[List[Tuple[int, int]]]:
    """Circle method. For even m, returns m-1 edge-disjoint perfect matchings
    that together cover every pair exactly once."""
    idx = list(range(m))
    rounds = []
    for _ in range(m - 1):
        pairs = [
            (min(idx[i], idx[m - 1 - i]), max(idx[i], idx[m - 1 - i]))
            for i in range(m // 2)
        ]
        rounds.append(pairs)
        idx = [idx[0]] + [idx[-1]] + idx[1:-1]  # rotate, holding idx[0] fixed
    return rounds


def _warm_start(n, k, num_weeks, parity_fail):
    """Construct a uniqueness-optimal schedule to seed the solver.

    Returns (week_pairs, bye_per_week) or None when no clean construction applies
    (the only gap is odd team count with odd k>=3, a rare corner left to the solver).
    """
    if not parity_fail:
        if n % 2 == 1:
            return None  # odd n with even k: skip warm start (corner case)
        rounds = _round_robin_rounds(n)  # n-1 disjoint matchings
        R = len(rounds)
        week_pairs = []
        for w in range(num_weeks):
            wp = []
            for slot in range(k):
                wp.extend(rounds[(w * k + slot) % R])  # k distinct rounds (k <= n-1)
            week_pairs.append(wp)
        return week_pairs, [None] * num_weeks

    # parity_fail => n odd and k odd; only k == 1 gets a clean one-bye-per-week build
    if k != 1:
        return None
    rounds = _round_robin_rounds(n + 1)  # dummy team index == n marks the bye
    dummy = n
    real_rounds, byes = [], []
    for rd in rounds:
        bye_team, pairs = None, []
        for (a, b) in rd:
            if a == dummy or b == dummy:
                bye_team = a if b == dummy else b
            else:
                pairs.append((a, b))
        real_rounds.append(pairs)
        byes.append(bye_team)
    R = len(real_rounds)
    week_pairs = [list(real_rounds[w % R]) for w in range(num_weeks)]
    bye_per_week = [byes[w % R] for w in range(num_weeks)]
    return week_pairs, bye_per_week


# --------------------------------------------------------------------------- #
# Result container
# --------------------------------------------------------------------------- #
class Schedule:
    """Holds the generated schedule plus summary metadata."""

    def __init__(self, teams: List[str]):
        self.teams = teams
        # weeks[w] -> list of (home, away, tier) tuples
        self.weeks: List[List[Tuple[str, str, str]]] = []
        self.byes: List[str] = []  # byes[w] -> team name or None
        self.unique_optimal = False
        self.affinity_optimal = False
        self.orientation_optimal = False

    # --- derived stats -----------------------------------------------------
    def total_matches(self) -> int:
        return sum(len(w) for w in self.weeks)

    def unique_matches(self) -> int:
        seen = set()
        for w in self.weeks:
            for home, away, _ in w:
                seen.add(frozenset((home, away)))
        return len(seen)

    def duplicate_matches(self) -> int:
        return self.total_matches() - self.unique_matches()

    def home_away_counts(self) -> Dict[str, Tuple[int, int]]:
        home = defaultdict(int)
        away = defaultdict(int)
        for w in self.weeks:
            for h, a, _ in w:
                home[h] += 1
                away[a] += 1
        return {t: (home[t], away[t]) for t in self.teams}

    def tier_counts(self) -> Dict[str, int]:
        counts = defaultdict(int)
        for w in self.weeks:
            for _, _, tier in w:
                counts[tier] += 1
        return dict(counts)


# --------------------------------------------------------------------------- #
# Core builder
# --------------------------------------------------------------------------- #
def build_schedule(
    matches_per_week: int,
    num_weeks: int,
    weekly_divisions: List[Dict[str, str]],
    *,
    allow_byes: bool = False,
    time_limit_s: float = 60.0,
    workers: int = 8,
    seed: int = 0,
) -> Schedule:
    """Build a season schedule. See module docstring for semantics."""

    # ---- validation -------------------------------------------------------
    if num_weeks != len(weekly_divisions):
        raise ValueError(
            f"num_weeks ({num_weeks}) != len(weekly_divisions) ({len(weekly_divisions)})."
        )
    if num_weeks == 0:
        raise ValueError("num_weeks must be >= 1.")

    teams = sorted(weekly_divisions[0].keys())
    n = len(teams)
    k = matches_per_week
    team_set = set(teams)

    for w, dmap in enumerate(weekly_divisions):
        if set(dmap.keys()) != team_set:
            raise ValueError(
                f"Week {w} roster differs from week 0; the roster must be constant."
            )

    if k < 1:
        raise ValueError("matches_per_week must be >= 1.")
    if k > n - 1:
        raise ValueError(
            f"matches_per_week ({k}) exceeds n-1 ({n - 1}); a team cannot play that "
            f"many DISTINCT opponents in one week. (Not fixable with byes.)"
        )

    parity_fail = (n * k) % 2 == 1
    if parity_fail and not allow_byes:
        raise ValueError(
            f"n*k is odd (n={n}, k={k}), so an exact-{k} week is impossible. "
            f"Set allow_byes=True to let one team play one fewer match per week."
        )

    pairs = list(combinations(range(n), 2))  # (i, j) with i < j

    # ---- matchup model ----------------------------------------------------
    model = cp_model.CpModel()

    # x[w, i, j] = 1 if teams i and j meet in week w
    x = {
        (w, i, j): model.NewBoolVar(f"x_{w}_{i}_{j}")
        for w in range(num_weeks)
        for (i, j) in pairs
    }

    # Optional bye variables (only when parity fails)
    bye = {}
    if parity_fail:
        for w in range(num_weeks):
            for i in range(n):
                bye[(w, i)] = model.NewBoolVar(f"bye_{w}_{i}")
            model.Add(sum(bye[(w, i)] for i in range(n)) == 1)  # one bye per week
        base = num_weeks // n
        for i in range(n):
            cnt = sum(bye[(w, i)] for w in range(num_weeks))
            model.Add(cnt <= base + 1)  # spread byes as evenly as possible
            model.Add(cnt >= base)

    # Degree constraint: each team plays exactly k (or k-1 if it has the bye)
    for w in range(num_weeks):
        for i in range(n):
            deg = sum(
                x[(w, min(i, j), max(i, j))] for j in range(n) if j != i
            )
            if parity_fail:
                model.Add(deg == k - bye[(w, i)])
            else:
                model.Add(deg == k)

    # Coverage variable u[i, j] = 1 if pair played at least once
    u = {(i, j): model.NewBoolVar(f"u_{i}_{j}") for (i, j) in pairs}
    for (i, j) in pairs:
        model.Add(u[(i, j)] <= sum(x[(w, i, j)] for w in range(num_weeks)))

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit_s
    solver.parameters.num_search_workers = workers
    solver.parameters.random_seed = seed

    result = Schedule(teams)

    num_pairs = len(pairs)
    matches_per_wk = (n * k - (1 if parity_fail else 0)) // 2
    total_matches = num_weeks * matches_per_wk
    ub_unique = min(total_matches, num_pairs)  # analytic max distinct matchups

    # ---- Division-affinity objective (the secondary goal) -----------------
    affinity = []
    for w in range(num_weeks):
        dmap = weekly_divisions[w]
        for (i, j) in pairs:
            s = TIER_SCORE[division_tier(dmap[teams[i]], dmap[teams[j]])]
            if s:
                affinity.append(s * x[(w, i, j)])

    warm = _warm_start(n, k, num_weeks, parity_fail)
    if warm is not None:
        # A construction reaching the analytic max exists: lock uniqueness at the
        # proven optimum and let the solver spend its budget on affinity, seeded
        # by the warm start so it always has a strong incumbent.
        week_pairs, bye_pw = warm
        used = {(w, i, j) for w, wp in enumerate(week_pairs) for (i, j) in wp}
        covered = {(i, j) for (_, i, j) in used}

        for key, var in x.items():
            model.AddHint(var, 1 if key in used else 0)
        for (i, j), var in u.items():
            model.AddHint(var, 1 if (i, j) in covered else 0)
        if parity_fail:
            for w, bt in enumerate(bye_pw):
                for i in range(n):
                    model.AddHint(bye[(w, i)], 1 if i == bt else 0)

        model.Add(sum(u.values()) == ub_unique)  # uniqueness proven-optimal
        result.unique_optimal = True
        model.Maximize(sum(affinity))
        status = solver.Solve(model)
    else:
        # Rare corner (odd team count, odd k>=3): weight uniqueness above all
        # achievable affinity so a single solve stays lexicographically correct.
        big = 2 * total_matches + 1
        model.Maximize(big * sum(u.values()) + sum(affinity))
        status = solver.Solve(model)
        result.unique_optimal = status == cp_model.OPTIMAL

    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        raise RuntimeError("No feasible schedule found (matchup stage).")
    result.affinity_optimal = status == cp_model.OPTIMAL

    # ---- extract chosen matchups -----------------------------------------
    chosen: List[List[Tuple[int, int]]] = []  # per week, list of (i, j)
    for w in range(num_weeks):
        wk = [(i, j) for (i, j) in pairs if solver.Value(x[(w, i, j)]) == 1]
        chosen.append(wk)

    bye_team_per_week: List = [None] * num_weeks
    if parity_fail:
        for w in range(num_weeks):
            for i in range(n):
                if solver.Value(bye[(w, i)]) == 1:
                    bye_team_per_week[w] = teams[i]
                    break

    # ---- Stage 3: assign home/away ---------------------------------------
    orient = _assign_home_away(
        chosen, n, num_weeks, time_limit_s, workers, seed
    )
    result.orientation_optimal = orient["optimal"]
    home_is_i = orient["home_is_i"]

    # ---- assemble result --------------------------------------------------
    for w in range(num_weeks):
        dmap = weekly_divisions[w]
        week_matches = []
        for (i, j) in chosen[w]:
            if home_is_i[(w, i, j)]:
                home, away = teams[i], teams[j]
            else:
                home, away = teams[j], teams[i]
            tier = division_tier(dmap[teams[i]], dmap[teams[j]])
            week_matches.append((home, away, tier))
        # stable, readable ordering
        week_matches.sort(key=lambda m: (m[0], m[1]))
        result.weeks.append(week_matches)
        result.byes.append(bye_team_per_week[w])

    return result


def _assign_home_away(chosen, n, num_weeks, time_limit_s, workers, seed):
    """Orientation sub-problem: minimize per-team home/away imbalance and flip
    the orientation of any pair that is played more than once."""
    model = cp_model.CpModel()

    # home_is_i[(w, i, j)] = 1 if i is home, else j is home
    h = {
        (w, i, j): model.NewBoolVar(f"h_{w}_{i}_{j}")
        for w in range(num_weeks)
        for (i, j) in chosen[w]
    }

    # per-team home count expression
    plays = defaultdict(int)
    home_terms = defaultdict(list)
    for w in range(num_weeks):
        for (i, j) in chosen[w]:
            plays[i] += 1
            plays[j] += 1
            home_terms[i].append(h[(w, i, j)])          # i home when h == 1
            home_terms[j].append(1 - h[(w, i, j)])       # j home when h == 0

    imbalance_terms = []
    for t in range(n):
        if plays[t] == 0:
            continue
        home_t = sum(home_terms[t])
        dev = model.NewIntVar(0, plays[t], f"dev_{t}")
        # |home - away| = |2*home - plays|
        model.Add(dev >= 2 * home_t - plays[t])
        model.Add(dev >= plays[t] - 2 * home_t)
        imbalance_terms.append(dev)

    # flip penalty for repeated pairs
    occ = defaultdict(list)
    for w in range(num_weeks):
        for (i, j) in chosen[w]:
            occ[(i, j)].append(h[(w, i, j)])
    flip_terms = []
    for (i, j), vs in occ.items():
        m = len(vs)
        if m < 2:
            continue
        s = sum(vs)
        pdev = model.NewIntVar(0, m, f"pdev_{i}_{j}")
        model.Add(pdev >= 2 * s - m)
        model.Add(pdev >= m - 2 * s)
        flip_terms.append(pdev)

    # balance dominates; flipping is a lighter secondary preference
    model.Minimize(10 * sum(imbalance_terms) + 1 * sum(flip_terms))

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit_s
    solver.parameters.num_search_workers = workers
    solver.parameters.random_seed = seed
    status = solver.Solve(model)
    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        raise RuntimeError("No feasible home/away assignment found.")

    return {
        "optimal": status == cp_model.OPTIMAL,
        "home_is_i": {key: bool(solver.Value(var)) for key, var in h.items()},
    }


# --------------------------------------------------------------------------- #
# Output helpers
# --------------------------------------------------------------------------- #
def print_schedule(schedule: Schedule, weekly_divisions: List[Dict[str, str]]) -> None:
    """Pretty-print the schedule and a summary block to stdout."""
    print("=" * 64)
    print("SEASON SCHEDULE")
    print("=" * 64)
    seen = set()
    for w, matches in enumerate(schedule.weeks):
        print(f"\nWeek {w + 1}")
        if schedule.byes[w]:
            print(f"  (bye: {schedule.byes[w]})")
        for home, away, tier in matches:
            pair = frozenset((home, away))
            dup = " [dup]" if pair in seen else ""
            seen.add(pair)
            dh = weekly_divisions[w][home]
            da = weekly_divisions[w][away]
            print(f"  {home} ({dh})  vs  {away} ({da})   [{tier}]{dup}")

    print("\n" + "=" * 64)
    print("SUMMARY")
    print("=" * 64)
    print(f"Teams:            {len(schedule.teams)}")
    print(f"Weeks:            {len(schedule.weeks)}")
    print(f"Total matches:    {schedule.total_matches()}")
    print(f"Unique matchups:  {schedule.unique_matches()}")
    print(f"Duplicates:       {schedule.duplicate_matches()}")
    print(f"Tier breakdown:   {schedule.tier_counts()}")
    print(
        f"Optimality:       unique={'opt' if schedule.unique_optimal else 'best-effort'}, "
        f"affinity={'opt' if schedule.affinity_optimal else 'best-effort'}, "
        f"home/away={'opt' if schedule.orientation_optimal else 'best-effort'}"
    )
    print("\nHome / Away balance per team:")
    for t, (hh, aa) in sorted(schedule.home_away_counts().items()):
        print(f"  {t:<18} home={hh:<3} away={aa:<3} (diff {hh - aa:+d})")


def write_csv(
    schedule: Schedule,
    weekly_divisions: List[Dict[str, str]],
    path: str,
) -> None:
    """Write the schedule to a CSV file."""
    seen = set()
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "week",
                "home",
                "away",
                "home_division",
                "away_division",
                "tier",
                "is_duplicate",
            ]
        )
        for w, matches in enumerate(schedule.weeks):
            for home, away, tier in matches:
                pair = frozenset((home, away))
                is_dup = pair in seen
                seen.add(pair)
                writer.writerow(
                    [
                        w + 1,
                        home,
                        away,
                        weekly_divisions[w][home],
                        weekly_divisions[w][away],
                        tier,
                        is_dup,
                    ]
                )


# --------------------------------------------------------------------------- #
# Demo
# --------------------------------------------------------------------------- #
if __name__ == "__main__":
    # Small illustrative example: 8 teams, 4 weeks, 1 match per team per week.
    base = {
        "Alpha": "East", "Bravo": "East", "Charlie": "East", "Delta": "East",
        "Echo": "West", "Foxtrot": "West", "Golf": "West", "Hotel": "West",
    }
    # Weeks 3-4: some teams shift divisions, including a combined division.
    shifted = {
        "Alpha": "East", "Bravo": "East/Central", "Charlie": "Central", "Delta": "East",
        "Echo": "West", "Foxtrot": "Central/West", "Golf": "West", "Hotel": "Central",
    }
    weekly = [base, base, shifted, shifted]

    sched = build_schedule(
        matches_per_week=1,
        num_weeks=4,
        weekly_divisions=weekly,
        allow_byes=False,
        time_limit_s=30,
    )
    print_schedule(sched, weekly)
    write_csv(sched, weekly, "schedule.csv")
    print("\nCSV written to schedule.csv")
