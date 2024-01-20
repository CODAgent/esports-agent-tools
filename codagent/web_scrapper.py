#### Esports Agent Inc
#### Brett O'Connor, Co-CEO

# Imports
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
import re

# FOR TESTING
# driver = webdriver.Chrome(ChromeDriverManager().install())

# TEST DATA
# 2v2 1ND FE NO PRIZE VG SND - 5 teams, Sept 5, 2022 at 8:30pm
# URL = "https://esportsagent.gg/tournament/11730036/overview" 

# Info 
# Date and time: div class="text-gray-500 uppercase text-sm font-roboto"
# Tourney title: span class="font-semibold text-2xl lg:text-3xl text-white"
# Per person: span class="font-semibold text-white" --> 0th
# Platforms
# Team size: span class="font-semibold text-white" --> 1st 
# Tournament type: span class="font-semibold text-white capitalize" 
# Players in match: span class="font-semibold text-white" --> 2nd 
# Teams Registered: span class="font-semibold text-white" --> 3rd 
# Game mode: span class="font-semibold text-white" --> 4th 
# Prize pool: span class="font-semibold text-white" --> 5th 

# Inputs: driver, tourney URL
# Returns: all the tournament's information
def get_tournament_info(driver, URL):
    driver.get(URL)
     
    soup = BeautifulSoup(driver.page_source, 'html.parser') 

    # Date and time (date_time)
    date_time_res = soup.find_all('div', {'class': 'text-gray-500 uppercase text-sm font-roboto'})
    date_time = date_time_res[0].text.strip()
    date_time_list = date_time.split()
    date = date_time_list[0] + " " + date_time_list[1] + " " + date_time_list[2]
    time = date_time_list[3] + " " + date_time_list[4]
    
    # Tourney title
    title_res = soup.find_all('span', {'class': 'font-semibold text-2xl lg:text-3xl max-w-[420px] break-words text-white'})
    if len(title_res) < 1:
        title_res = soup.find_all('span', {'class': 'font-semibold text-2xl lg:text-3xl max-w-[420px] break-words text-gold'})
        if len(title_res) < 1:
            title = 'title error'
        else: 
            title = title_res[0].text.strip()
    else:
        title = title_res[0].text.strip()
    
    # Per person
    per_person_res = soup.find_all('span', {'class': 'font-semibold text-white'})
    per_person = per_person_res[0].text.strip()
    
    # Platforms
    # xbox_logo = "https://esportsagent.gg/_next/image?url=%2Fassets%2Fimages%2Fplatforms%2Fxbox.png&w=32&q=75"
    xbox_logo = "xbox"
    ps_logo = "playstation" 
    battle_net_logo = "battle.net" 
    steam_logo = "steam"
    xbox_res = soup.find_all(srcset=re.compile(xbox_logo))
    ps_res = soup.find_all(srcset=re.compile(ps_logo))
    battle_net_res = soup.find_all(srcset=re.compile(battle_net_logo))
    platforms = []
    if xbox_res is not None:
        platforms.append(xbox_logo)
    if ps_res is not None:
        platforms.append(ps_logo)
    if battle_net_res is not None:
        platforms.append(battle_net_logo)
    
    # Team size
    team_size_res = soup.find_all('span', {'class': 'font-semibold text-white'})
    team_size = team_size_res[1].text.strip()
    
    # Tournament type
    tournament_type_res = soup.find_all('span', {'class': 'font-semibold text-white capitalize'})
    tournament_type = tournament_type_res[0].text.strip()
    
    # Players in match
    players_in_match_res = soup.find_all('span', {'class': 'font-semibold text-white'})
    players_in_match = players_in_match_res[2].text.strip()
    
    # Teams Registered
    teams_registered_res = soup.find_all('span', {'class': 'font-semibold text-white'})
    teams_registered = teams_registered_res[3].text.strip()
    
    # Game mode
    gamemode_res = soup.find_all('span', {'class': 'font-semibold text-white'})
    gamemode = gamemode_res[4].text.strip()
    
    # Prize pool
    prize_pool_res = soup.find_all('span', {'class': 'font-semibold text-white'})
    prize_pool = prize_pool_res[5].text.strip()

    info = {"date": date, "time": time, "title": title, "per_person": per_person, "platforms": platforms,"team_size": team_size, "tournament_type": tournament_type, "players_in_match": players_in_match, "teams_registered": teams_registered, "gamemode": gamemode, "prize_pool": prize_pool}

    return info

# print(get_tournament_info(driver, URL))

# TEST DATA
# tourney_ids = [11737409, 11739353, 11737386]

# FOR TESTING
# Note: no slash after tournament
# URL_begin = "https://esportsagent.gg/tournament"  
# driver.get(URL_begin)
    
# Inputs: driver, URL_begin 
# Returns: a list of the end of the links of past codagent tourneys visible on our site
# Note: esportsagent.gg returns <Response [500]> if there is a broken link 
def get_tournament_ids(driver, URL_begin):
    id_list = []
    driver.get(URL_begin)

    past_tournaments = None
    while(not(past_tournaments)):
        print("Waiting for site to load")
        soup = BeautifulSoup(driver.page_source, 'html.parser') 
        past_tournaments = soup.find_all('div', {'class': 'mt-4 md:mt-6 grid md:grid-cols-2 lg:grid-cols-3 gap-4'})

    print("Site has loaded")
    
    for c in past_tournaments[0].children:
        a = c.find('a')
        id_list.append(a.get('href'))
    return id_list

# print(get_tournament_ids(driver, URL_begin))
