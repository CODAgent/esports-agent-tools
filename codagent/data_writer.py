#### Esports Agent Inc
#### Brett O'Connor, Co-CEO

# Imports
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
import re
import csv

# FOR TEST
# might not need this import when we're done making this
from main import get_all_info


# FOR TEST 
tournament_ids = ["/tournament/11763661", "/tournament/11763657"]
driver = webdriver.Chrome(ChromeDriverManager().install())
URL_begin = "https://esportsagent.gg/tournament" 
URL_all_info = "https://esportsagent.gg"

data = get_all_info(tournament_ids, driver, URL_all_info)

# TEST DATA
# test_data = [{'date': 'September 12, 2022', 'time': '10:20 PM', 'title': '2v2 1ND MW SND', 'per_person': '$4', 'platforms': ['xbox', 'playstation', 'battle.net'], 'team_size': '2', 'tournament_type': 'single elimination', 'players_in_match': '2v2', 'teams_registered': '2', 'gamemode': 'Best of 1', 'prize_pool': '$14'}, {'date': 'September 12, 2022', 'time': '9:20 PM', 'title': '3v3 1ND CW SND', 'per_person': '$4', 'platforms': ['xbox', 'playstation', 'battle.net'], 'team_size': '3', 'tournament_type': 'single elimination', 'players_in_match': '3v3', 'teams_registered': '4', 'gamemode': 'Best of 1', 'prize_pool': '$33'}]


# Write all data to CSV file
# Input: data to write, path (optional, default is "all_data.csv")
# Returns: None 
def write_all(data, path="all_data.csv"):
    header = ['Date', 'Time', 'Title', 'Buy-in Per Player', 'Platforms', 'Team Size', 'Tournament Type (Ex: Single Elimination)', 'Players in Match', 'Number of Teams Registered', 'Series Type (Ex: Best of 3)', 'Prize Pool']
    field_names = ['date', 'time', 'title', 'per_person', 'platforms', 'team_size', 'tournament_type', 'players_in_match', 'teams_registered', 'gamemode', 'prize_pool']
    with open(path, 'w') as f:
        writer = csv.writer(f)

        writer.writerow(header)

        dict_writer = csv.DictWriter(f, fieldnames=field_names)

        # for d in data:
        #     dict_writer.writerows(d)
        dict_writer.writerows(data)

    print("DONE")
    return None


# write_all(test_data)
# write_all(data)
    
