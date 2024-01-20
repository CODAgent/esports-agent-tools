#### Esports Agent Inc
#### Brett O'Connor, Co-CEO

## Main script to harvest our tournament data

# Imports
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import requests
import re


#### MAIN FUNCTION ####
def main(backup_data=False, data_file_path='all_data.csv', backup_data_file_path='backup_all_data.csv', current_stored_data_file_path='all_data.csv'):
    # FOR TEST
    # main_path = 'all_data.csv'
    # backup_path = 'backup_all_data.csv'
    # filter_path = 'filtered_data.csv'
    # filter_input_1 = 'date'
    # filter_input_2 = ['September 22, 2022', 'September 22, 2022']

    if not(backup_data):
        # Chrome (not working right now)
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        
        # Firefox (works with my linux machine)
        firefox_options = Options()
        firefox_options.set_preference('permissions.default.image', 2)
        firefox_options.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
        driver = webdriver.Firefox(options=firefox_options)

        challonge_URL_begin = "https://challonge.com/users/esportsagent/tournaments"
        esportsagent_URL_begin = "https://esportsagent.gg/tournament" 

        # read in previously stored data

        # see what date we need to search challonge stuff for 

        # might be able to just use the challonge API
        # go to challonge site and get these tourney IDs

        # go to challonge tourneys and get number of teams enetered 

        # go to esports agent tourneys and get the rest of the values needed 



        # tourney_ids = get_tournament_ids(driver, URL_begin)
        # all_info = get_all_info(tourney_ids, driver, URL_all_info)

        # write_all(all_info, path=main_path)
        # add_profit(main_path)
        
    else:
        # create_backup(main_path, backup_path)

main()
