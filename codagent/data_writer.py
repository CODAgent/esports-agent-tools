#### Esports Agent Inc
#### Brett O'Connor, Co-CEO

# Imports
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
import re
import csv
import os

# FOR TEST
# might not need this import when we're done making this
# from main import get_all_info


# FOR TEST 
# tournament_ids = ["/tournament/11763661", "/tournament/11763657"]
# driver = webdriver.Chrome(ChromeDriverManager().install())
# URL_begin = "https://esportsagent.gg/tournament" 
# URL_all_info = "https://esportsagent.gg"
# 
# data = get_all_info(tournament_ids, driver, URL_all_info)

# TEST DATA
test_data = [{'date': 'September 12, 2022', 'time': '10:20 PM', 'title': '2v2 1ND MW SND', 'per_person': '$4', 'platforms': ['xbox', 'playstation', 'battle.net'], 'team_size': '2', 'tournament_type': 'single elimination', 'players_in_match': '2v2', 'teams_registered': '2', 'gamemode': 'Best of 1', 'prize_pool': '$14'}, {'date': 'September 12, 2022', 'time': '9:20 PM', 'title': '3v3 1ND CW SND', 'per_person': '$4', 'platforms': ['xbox', 'playstation', 'battle.net'], 'team_size': '3', 'tournament_type': 'single elimination', 'players_in_match': '3v3', 'teams_registered': '4', 'gamemode': 'Best of 1', 'prize_pool': '$33'}]
test_data_2 = [{'date': 'September 13, 2022', 'time': '10:22 PM', 'title': '3v3 1ND MW SND', 'per_person': '$8', 'platforms': ['xbox', 'playstation', 'battle.net'], 'team_size': '2', 'tournament_type': 'single elimination', 'players_in_match': '3v3', 'teams_registered': '4', 'gamemode': 'Best of 1', 'prize_pool': '$28'}, {'date': 'September 12, 2022', 'time': '9:20 PM', 'title': '3v3 1ND CW SND', 'per_person': '$4', 'platforms': ['xbox', 'playstation', 'battle.net'], 'team_size': '3', 'tournament_type': 'single elimination', 'players_in_match': '3v3', 'teams_registered': '4', 'gamemode': 'Best of 1', 'prize_pool': '$33'}]


# Write all data to CSV file
# Input: data to write, path (optional, default is "all_data.csv")
# Returns: None 
# Prints out status messages
    # "Done.  New file created." 
    # "Done.  New data written."
    # "Done.  No new data written."
def write_all(data, path="all_data.csv"):
    # header for the csv file 
    header = ['Date', 'Time', 'Title', 'Buy-in Per Player', 'Platforms', 'Team Size', 'Tournament Type (Ex: Single Elimination)', 'Players in Match', 'Number of Teams Registered', 'Series Type (Ex: Best of 3)', 'Prize Pool']
    field_names = ['date', 'time', 'title', 'per_person', 'platforms', 'team_size', 'tournament_type', 'players_in_match', 'teams_registered', 'gamemode', 'prize_pool']

    # Case: 'all data' file does not exist
    if not(os.path.isfile(path)):
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            dict_writer = csv.DictWriter(f, fieldnames=field_names)
            dict_writer.writerows(data)

        print("Done.  New file created.")
        return None

    # Case: 'all data' file exists
    else: 
        with open(path, 'r') as fr:
            read_data = []
            reader = csv.reader(fr)

            for line in reader:
                if line[4] != 'Platforms':
                    line[4] = eval(line[4])
                read_data.append(line)

            # get rid of header info because it is not needed
            read_data = read_data[1:len(read_data)]

            # For debugging
            # print('read_data: ', read_data)
            # print('write_data: ', list(data[0].values())) # gets dict values as list (for comparing use np.array_equal())

            # compare each new data value with read_data, if it is the same, ignore it, if not, write it 
            OVERALL_WRITE = 0
            WRITE_FLAG = 0
            new_data = []
            for d in data: 
                d_vals = list(d.values())
                for rd in read_data:
                    if rd == d_vals:
                        # skip the existing data, disable write flag
                        WRITE_FLAG = 0
                        break
                    else: 
                        # enable write flag
                        WRITE_FLAG = 1
                if WRITE_FLAG:
                    # prepare to write data
                    new_data.append(d_vals)
                    OVERALL_WRITE = 1
                    WRITE_FLAG = 0
                # else:
                    # skip data

        all_data = read_data + new_data
        if OVERALL_WRITE:
            # writing data
            with open(path, 'w', newline='') as fw:
                writer = csv.writer(fw)
                writer.writerow(header)
                for ad in all_data:
                    writer.writerow(ad)
                print("Done.  New data written.")
                return None
        else:
            print("Done.  No new data written.")

        return None


# FOR TEST
# write_all(test_data)
# write_all(test_data_2)
# write_all(data)
    
# Inputs: None
# Returns: a dict that maps as such --> {<filter category>: <array of acceptable filter criterion>, ....}
# Prints the return as well
def get_valid_filter_terms():
    valids = {'date': ['day-month-year'], 'money': ['free entry', 'paid entry', 'free entry no prize'], 'platforms': ['console only', 'pc only', 'all'], 'team size': ['1v1', '2v2', '3v3', '4v4'], 'elimination type': ['single', 'double'], 'number of teams': ['threshold value'], 'series type': ['bo1', 'bo3', 'bo5'], 'prize': ['threshold value'] }
    print("The following mapping are the valid categories and their respective criterion to be used for filtering: ")
    print(valids)
    return valids

# FOR TEST 
# get_valid_filter_terms()

# Inputs: path to all data file, filter category, filter criterion, output file name
# Returns: None
# Prints out status messages
    # "Done.  Filtered file created." 
    # "Invalid filter category.  No filtered file created."
    # "Invalid filter criterion.  No filtered file created."
def filter_write():
    return None
