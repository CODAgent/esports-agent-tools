#### Esports Agent Inc
#### Brett O'Connor, Co-CEO

# Imports
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
import re

from web_scrapper import get_tournament_info, get_tournament_ids   
from data_writer import write_all


# FOR TEST
# driver = webdriver.Chrome(ChromeDriverManager().install())
# URL_begin = "https://esportsagent.gg/tournament" 
# URL_all_info = "https://esportsagent.gg"

# TEST DATA
# tourney_ids = [11747364, 11749152]


# Inputs: tourney_ids (list of tournament ids based on challonge id), driver, beginning of URL
# Returns: all tournament info for inputted tourney ids
# Note: last part of the URL should be '<id>/overview'
def get_all_info(tourney_ids, driver, URL_begin):
    all_info = []
    for i in range(len(tourney_ids)):
        URL = URL_begin + str(tourney_ids[i]) + "/overview"
        driver.get(URL)
        print(tourney_ids[i])
        print("page rendered")

        all_info.append(get_tournament_info(driver, URL))

    return all_info

# FOR TEST
# print(len(get_all_info(tourney_ids, driver, URL_all_info)))





#### MAIN FUNCTION ####
def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())

    URL_begin = "https://esportsagent.gg/tournament" 
    URL_all_info = "https://esportsagent.gg"

    tourney_ids = get_tournament_ids(driver, URL_begin)
    all_info = get_all_info(tourney_ids, driver, URL_all_info)

    # path = 'all_data.csv'
    write_all(all_info)


main()

