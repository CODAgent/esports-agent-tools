#### Esports Agent Inc
#### Brett O'Connor, Co-CEO

# Imports
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import requests
import re

from web_scrapper import get_tournament_info, get_tournament_ids   
from data_writer import write_all, create_backup, filter_write, get_valid_filter_terms, add_profit


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

def define_action(action):
    return action 


#### MAIN FUNCTION ####
def main(action=None, filter_input_1=None, filter_input_2=None, main_path='all_data.csv', filter_path='filtered_data.csv', backup_path='backup_all_data.csv'):
    # FOR TEST
    # main_path = 'all_data.csv'
    # backup_path = 'backup_all_data.csv'
    # filter_path = 'filtered_data.csv'
    # filter_input_1 = 'date'
    # filter_input_2 = ['September 22, 2022', 'September 22, 2022']

    if action == None:
        ######################################################
        ######## EDIT THIS TO DO WHAT YOU WANT TO DO ######### 
        ######################################################
        # Options: 'mine', 'how to filter', 'filter', 'backup'
        action = define_action('mine')
        ######################################################
        ######################################################
        ######################################################

    if action == 'mine':
        # Chrome (not working right now)
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        
        # Firefox (works with my linux machine)
        firefox_options = Options()
        firefox_options.set_preference('permissions.default.image', 2)
        firefox_options.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
        driver = webdriver.Firefox(options=firefox_options)

        URL_begin = "https://esportsagent.gg/tournament" 
        URL_all_info = "https://esportsagent.gg"

        tourney_ids = get_tournament_ids(driver, URL_begin)
        all_info = get_all_info(tourney_ids, driver, URL_all_info)

        write_all(all_info, path=main_path)
        add_profit(main_path)
        
    if action == 'how to filter':
        get_valid_filter_terms()

    if action == 'filter':
        # filter_write(column_title, ['filter values']) --> see readme for more instructions
        filter_write(filter_input_1, filter_input_2, path=main_path, output_path=filter_path)

    if action == 'backup':
        create_backup(main_path, backup_path)


main()

