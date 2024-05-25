## Generate a schedule for CXP!

# imports 
import csv
import os
import numpy as np
import pandas as pd


SIGNUP_CSV_FILE = '2023-2024_signups/CXP_2023-2024_Season_Signups.csv'

VARSITY_FILE = '2023-2024_signups/CXP_2023_24_Varsity.csv'
OPEN_FILE = '2023-2024_signups/CXP_2023_24_Open.csv'
CLUB_FILE = '2023-2024_signups/CXP_2023_24_Club.csv'

SCHEDULE_FOLDER = '2023-2024_schedules'

varsity_dict = {"team": [], "division": []}
open_dict = {"team": [], "division": []}
club_dict = {"team": [], "division": []}

## Read ins
# Varsity 
with open(VARSITY_FILE, 'r', encoding='utf8') as f_varsity:
    reader_varsity = csv.reader(f_varsity)
    
    for idx, line in enumerate(reader_varsity):
        if idx == 0:
            continue
        varsity_dict["team"].append(line[0])
        varsity_dict["division"].append(line[2])

# Open 
with open(OPEN_FILE, 'r', encoding='utf8') as f_open:
    reader_open = csv.reader(f_open)
    
    for idx, line in enumerate(reader_open):
        if idx == 0:
            continue
        open_dict["team"].append(line[0])
        open_dict["division"].append(line[2])

# Club 
with open(CLUB_FILE, 'r', encoding='utf8') as f_club:
    reader_club = csv.reader(f_club)
    
    for idx, line in enumerate(reader_club):
        if idx == 0:
            continue
        club_dict["team"].append(line[0])
        club_dict["division"].append(line[2])


print('Total Number of Teams:')
print(len(varsity_dict["team"]) + len(open_dict["team"]) + len(club_dict["team"]))
print('---')
print('Number of Varsity Teams:')
print(len(varsity_dict["team"]))
print('Number of Open Teams:')
print(len(open_dict["team"]))
print('Number of Club Teams:')
print(len(club_dict["team"]))


# get unique divisions 
varsity_divisions = np.unique(varsity_dict["division"])
open_divisions = np.unique(open_dict["division"])
club_divisions = np.unique(club_dict["division"])

# make schedules for each division 
matches_per_week                = 2
regular_season_weeks            = 6
total_matches_per_team_goal     = matches_per_week * regular_season_weeks   # 12 (if more we trim, if less we duplicate beginning at the top)

total_varsity_matches         = {}
tmp_total_varsity_matches     = {}
for division in varsity_divisions:
    total_varsity_matches[division] = []
    tmp_total_varsity_matches[division] = []
varsity_matches_per_team      = {}
varsity_team_matches          = {}
tmp_varsity_team_matches          = {}
for team in varsity_dict["team"]:
    varsity_matches_per_team[team] = 0
    varsity_team_matches[team] = []
    tmp_varsity_team_matches[team] = []

total_open_matches            = {}
tmp_total_open_matches     = {}
for division in open_divisions:
    total_open_matches[division] = []
    tmp_total_open_matches[division] = []
open_matches_per_team         = {}
open_team_matches             = {}
tmp_open_team_matches             = {}
for team in open_dict["team"]:
    open_matches_per_team[team] = 0
    open_team_matches[team] = []
    tmp_open_team_matches[team] = []

total_club_matches            = {}
tmp_total_club_matches     = {}
for division in club_divisions:
    total_club_matches[division] = []
    tmp_total_club_matches[division] = []
club_matches_per_team         = {}
club_team_matches             = {}
tmp_club_team_matches             = {}
for team in club_dict["team"]:
    club_matches_per_team[team] = 0
    club_team_matches[team] = []
    tmp_club_team_matches[team] = []


# VARSITY 
for dd in range(len(varsity_divisions)):
    curr_division = varsity_divisions[dd]
    # teams only play each other if theyre in the same division
    for ii in range(len(varsity_dict["team"])):
        team1           = varsity_dict["team"][ii]
        division1       = varsity_dict["division"][ii]
        if division1 != curr_division:
            continue
        for jj in range(len(varsity_dict["team"])):

            team2           = varsity_dict["team"][jj]
            division2       = varsity_dict["division"][jj]
            if division2 != curr_division:
                continue

            if team1 == team2:
                continue 
            
            potential_match_name = team1 + ' vs ' + team2
            reverse_potential_match_name = team2 + ' vs ' + team1
            if (potential_match_name not in total_varsity_matches[curr_division]) and (reverse_potential_match_name not in total_varsity_matches[curr_division]):
                varsity_matches_per_team[team1] += 1
                varsity_matches_per_team[team2] += 1
                total_varsity_matches[curr_division].append(potential_match_name)
                varsity_team_matches[team1].append(potential_match_name)
                varsity_team_matches[team2].append(potential_match_name)


# get list of teams with less than 12 matches --> probably want this in a function 
def teams_in_need(varsity_matches_per_team, varsity_dict):
    teams_less_than_goal = {'team_name': [], 'division': []} 
    for idx, team_name in enumerate(varsity_matches_per_team.keys()):
        if varsity_matches_per_team[team_name] < total_matches_per_team_goal:
            teams_less_than_goal['team_name'].append(team_name)
            teamInd = varsity_dict["team"].index(team_name)
            teams_less_than_goal['division'].append(varsity_dict["division"][teamInd])

    teams_less_than_goal['team_name'] = np.array(teams_less_than_goal['team_name'])
    teams_less_than_goal['division'] = np.array(teams_less_than_goal['division'])

    return teams_less_than_goal

teams_less_than_goal = teams_in_need(varsity_matches_per_team, varsity_dict)
for div_idx, division in enumerate(varsity_divisions):
    inds_of_interest = np.where(teams_less_than_goal['division'] == division)

    # go thru teams in the same division that need matches 
    for team_inds in inds_of_interest[0]:
        for team_inds2 in inds_of_interest[0]:
            if team_inds == team_inds2:
                continue

            while(len(teams_less_than_goal['team_name']) != 0):
                print('in need teams')
                print(teams_less_than_goal['team_name'])
                            
                team1 = teams_less_than_goal['team_name'][team_inds]
                team2 = teams_less_than_goal['team_name'][team_inds2]

                potential_match_name = team1 + ' vs ' + team2
                reverse_potential_match_name = team2 + ' vs ' + team1
                varsity_matches_per_team[team1] += 1
                varsity_matches_per_team[team2] += 1
                total_varsity_matches[curr_division].append(potential_match_name)
                varsity_team_matches[team1].append(potential_match_name)
                varsity_team_matches[team2].append(potential_match_name)
    
                teams_less_than_goal = teams_in_need(varsity_matches_per_team, varsity_dict)





# # 12/10 --> need 2 more matches but we need them from teams that also dont have enough matches 
# for ii in range(len(varsity_dict["team"])):
#     # do calculations 
#     mod_val = total_matches_per_team_goal % varsity_matches_per_team[varsity_dict["team"][ii]]
#     int_divide_val = np.floor(total_matches_per_team_goal / varsity_matches_per_team[varsity_dict["team"][ii]])

    # if int_divide_val is larger than 1 we at minimum need to cycle thru the number of int_divide_vals
    # if mod val is zero, we are done after this cycle thru
    # if mod val is not zero, we need to cycle thru mod val times 

# # loop thru varsity_matches_per_team and if they are below 12 then start adding duplicates (see what multiple it is to see how often I need to add duplicates, use MOD)
# # maybe use a while loop
# for aa, overall_team in enumerate(varsity_matches_per_team.keys()):
#     # test = varsity_dict["team"].index(team)
# 
#     while varsity_matches_per_team[overall_team] < total_matches_per_team_goal:
#         for bb, team in enumerate(varsity_matches_per_team.keys()):
#             if varsity_matches_per_team[team] == total_matches_per_team_goal:
#                 continue
#             for cc, second_team in enumerate(varsity_matches_per_team.keys()):
# 
#                 team1           = team
#                 team1Ind        = varsity_dict["team"].index(team1)
#                 division1       = varsity_dict["division"][team1Ind]
# 
#                 team2           = second_team
#                 team2Ind        = varsity_dict["team"].index(team2)
#                 division2       = varsity_dict["division"][team2Ind]
# 
#                 if team1 == team2:
#                     continue 
#                 elif division1 != division2:
#                     continue 
#                 
#         
#                 potential_match_name = team1 + ' vs ' + team2
#                 reverse_potential_match_name = team2 + ' vs ' + team1
#                 # if (potential_match_name not in tmp_total_varsity_matches[division1]) and (reverse_potential_match_name not in tmp_total_varsity_matches[division1]):
#                 if varsity_matches_per_team[team2] == total_matches_per_team_goal:
#                     continue
#                 varsity_matches_per_team[team1] += 1
#                 varsity_matches_per_team[team2] += 1
#                 tmp_total_varsity_matches[division1].append(potential_match_name)
#                 tmp_varsity_team_matches[team1].append(potential_match_name)
#                 tmp_varsity_team_matches[team2].append(potential_match_name)
# 
# for xx, team in enumerate(tmp_varsity_team_matches.keys()):
#     varsity_team_matches[team] = varsity_team_matches[team] + tmp_varsity_team_matches[team]
# 
# for xx, division in enumerate(tmp_total_varsity_matches.keys()):
#     total_varsity_matches[division] = total_varsity_matches[division] + tmp_total_varsity_matches[division]

    
    

varsity_check = {}

for division in varsity_divisions:
    varsity_check[division] = {}

    for aa in range(len(varsity_dict["team"])):
        if varsity_dict["division"][aa] == division:
            varsity_check[division][varsity_dict["team"][aa]] = varsity_matches_per_team[varsity_dict["team"][aa]]

print('***')
print(total_varsity_matches)
print('***')
print('---')
print(varsity_team_matches)
print('---')

# print(varsity_check)
# print(total_varsity_matches)
print(varsity_matches_per_team)

total_varsity_matches_df = pd.DataFrame.from_dict(total_varsity_matches, orient='index')
total_varsity_matches_df.to_csv("test.csv", header=False)
# with open('test.csv', 'w', newline='') as csv_varsity:
#     varsity_writer = csv.writer(csv_varsity)
#     varsity_writer.writerow(total_varsity_matches.keys())
#     varsity_writer.writerows(zip(*total_varsity_matches.values()))

# print(len(varsity_team_matches))
# print(len(np.unique(varsity_team_matches)))

# OPEN 



# CLUB





# ---

# # read in signup file
# team_dict = {"team": [], "league": []}
# with open(SIGNUP_CSV_FILE, 'r', encoding='utf8') as fr:
#     reader = csv.reader(fr)
# 
#     for idx, line in enumerate(reader):
#         # skip header
#         if idx == 0:
#             continue
#         team_dict["team"].append(line[1])
#         team_dict["league"].append(line[len(line) - 3])
# 
# # clean up league info
# for ii, item in enumerate(team_dict["league"]):
#     if "Varsity" in team_dict["league"][ii]:
#         team_dict["league"][ii] = 'varsity'
#     elif "Club" in team_dict["league"][ii]:
#         team_dict["league"][ii] = 'club'
#     elif "Open" in team_dict["league"][ii]:
#         team_dict["league"][ii] = 'open'
# 
# varisty_teams = []
# open_teams = []
# club_teams = []
# 
# for jj, team_name in enumerate(team_dict["team"]):
#     if team_dict["league"][jj] == 'varsity':
#         varisty_teams.append(team_name)
#     elif team_dict["league"][jj] == 'open':
#         open_teams.append(team_name)
#     elif team_dict["league"][jj] == 'club':
#         club_teams.append(team_name)
# 
# print('Total Number of Teams:')
# print(len(varisty_teams) + len(open_teams) + len(club_teams))
# print('---')
# print('Number of Varsity Teams:')
# print(len(varisty_teams))
# print('Number of Open Teams:')
# print(len(open_teams))
# print('Number of Club Teams:')
# print(len(club_teams))



