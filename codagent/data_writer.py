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
import shutil

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

# Input: file path, back up file path
# Returns: None
# Prints a successful message when done
def create_backup(file_path, backup_file_path):
    shutil.copy(file_path, backup_file_path)
    print("Backup has been created at: ", backup_file_path)
    return None

# FOR TEST
# file_path = './all_data.csv'
# backup_file_path = './backup_all_data.csv'
# create_backup(file_path, backup_file_path)

# Write all data to CSV file
# Input: data to write, path (optional, default is "all_data.csv")
# Returns: None 
# Prints out status messages
    # "Done.  New file created." 
    # "Done.  New data written."
    # "Done.  No new data written."
def write_all(data, path="all_data.csv"):
    backup_path = "backup_" + path
    # header for the csv file 
    header = ['Date', 'Time', 'Title', 'Buy-in Per Player', 'Platforms', 'Team Size', 'Tournament Type (Ex: Single Elimination)', 'Players in Match', 'Number of Teams Registered', 'Series Type (Ex: Best of 3)', 'Prize Pool']
    field_names = ['date', 'time', 'title', 'per_person', 'platforms', 'team_size', 'tournament_type', 'players_in_match', 'teams_registered', 'gamemode', 'prize_pool']

    # Case: 'all data' file does not exist
    if not(os.path.isfile(path)):
        with open(path, 'w', newline='', errors='ignore') as f:
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
            with open(path, 'w', newline='', errors='ignore') as fw:
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
    valids = {'date': ['month day, year', 'month year', 'year'], 'money': ['free entry', 'paid entry', 'free entry no prize'], 'platforms': ['console only', 'pc only', 'all'], 'team size': ['1v1', '2v2', '3v3', '4v4', '5v5', '6v6'], 'elimination type': ['single', 'double'], 'number of teams': ['threshold value'], 'series type': ['bo1', 'bo3', 'bo5'], 'prize': ['threshold value'] }
    print("The following mapping are the valid categories and their respective criterion to be used for filtering: ")
    print(valids)
    return valids

# FOR TEST 
# get_valid_filter_terms()

# Inputs: path to all data file, filter category, filter criterion
# Returns: None
# Prints out status messages
    # "Done.  Filtered file created." 
    # "Invalid filter category.  No filtered file created."
    # "Invalid filter criterion.  No filtered file created."
def filter_write(filter_category, filter_criterion, path='all_data.csv', output_path='filtered_data.csv'):
    # header info
    header = ['Date', 'Time', 'Title', 'Buy-in Per Player', 'Platforms', 'Team Size', 'Tournament Type (Ex: Single Elimination)', 'Players in Match', 'Number of Teams Registered', 'Series Type (Ex: Best of 3)', 'Prize Pool']

    # date looks for either:
    # (1) a start day-month-year and an end day-month-year
    # (2) a month-year
    # (3) a year
    # expected input for 'filter_criterion' is a list
    if filter_category == "date":
        # filter_path = 'filtered_by_date.csv'
        month_map = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
        # month_map = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
        # for case (1)
        if len(filter_criterion) == 2:
            start = filter_criterion[0].split(' ')
            start_day = start[1][0:len(start[1])-1]
            start_day_num = int(start_day)
            start_month_num = month_map[start[0]]
            start_year_num = int(start[2])

            end = filter_criterion[1].split(' ')
            end_day = end[1][0:len(end[1])-1]
            end_day_num = int(end_day)
            end_month_num = month_map[end[0]]
            end_year_num = int(end[2])
            
            data = []
            with open(path, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    row_date = row['Date'].split(' ')
                    row_day = int(row_date[1][0:len(row_date[1])-1])
                    if int(row_date[2]) >= start_year_num and int(row_date[2]) <= end_year_num:
                        if month_map[row_date[0]] >= start_month_num and month_map[row_date[0]] <= end_month_num:
                            if row_day >= start_day_num and row_day <= end_day_num:
                                data.append(row)
            with open(output_path, 'w', newline='') as fw:
                writer = csv.DictWriter(fw, fieldnames=header)
                writer.writeheader()
                for d in data: 
                    writer.writerow(d)

            print("Filtered by date file created.")

                    
        if len(filter_criterion) == 1:
            date = filter_criterion[0].split(' ') 

            # for case (2)
            if len(date) == 2:
                month_num = month_map[date[0]]
                year_num = int(date[1])

                data = []
                with open(path, 'r') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        row_date = row['Date'].split(' ')
                        if int(row_date[2]) == year_num:
                            if month_map[row_date[0]] == month_num:
                                data.append(row)
                with open(output_path, 'w', newline='') as fw:
                    writer = csv.DictWriter(fw, fieldnames=header)
                    writer.writeheader()
                    for d in data: 
                        writer.writerow(d)

                print("Filtered by date file created.")

            # # for case (3)
            if len(date) == 1:
                year_num = int(date[0])

                data = []
                with open(path, 'r') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        row_date = row['Date'].split(' ')
                        if int(row_date[2]) == year_num:
                                data.append(row)
                with open(output_path, 'w', newline='') as fw:
                    writer = csv.DictWriter(fw, fieldnames=header)
                    writer.writeheader()
                    for d in data: 
                        writer.writerow(d)

                print("Filtered by date file created.")


    # money (buy-in) looks for either:
    # (1) free entry --> buy-in = $0
    # (2) paid entry --> buy-in > $0
    # (3) free entry no prize --> buy-in = $0 and prize = $0
    # (4) a threshold amount --> Ex: '>,5' or '<,5' format: '<greater than or less than>,<value>'
    # expected input for 'filter_criterion' is a list
    if filter_category == "money":
        if filter_criterion[0] == "free entry":
            data = []
            with open(path, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    row_buy = row['Buy-in Per Player'].split('$')
                    row_buy_int = float(row_buy[1])
                    if row_buy_int == 0.0:
                            data.append(row)
            with open(output_path, 'w', newline='') as fw:
                writer = csv.DictWriter(fw, fieldnames=header)
                writer.writeheader()
                for d in data: 
                    writer.writerow(d)

            print("Filtered by buy-in file created.")

        if filter_criterion[0] == "paid entry":
            data = []
            with open(path, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    row_buy = row['Buy-in Per Player'].split('$')
                    row_buy_int = float(row_buy[1])
                    if row_buy_int > 0.0:
                            data.append(row)
            with open(output_path, 'w', newline='') as fw:
                writer = csv.DictWriter(fw, fieldnames=header)
                writer.writeheader()
                for d in data: 
                    writer.writerow(d)

            print("Filtered by buy-in file created.")

        if filter_criterion[0] == "free entry no prize":
            data = []
            with open(path, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    row_buy = row['Buy-in Per Player'].split('$')
                    row_buy_int = float(row_buy[1])
                    row_prize = row['Prize Pool'].split('$')
                    row_prize_int = float(row_prize[1])
                    if row_buy_int == 0.0 and row_prize_int == 0.0:
                            data.append(row)
            with open(output_path, 'w', newline='') as fw:
                writer = csv.DictWriter(fw, fieldnames=header)
                writer.writeheader()
                for d in data: 
                    writer.writerow(d)

            print("Filtered by buy-in file created.")

        if len(filter_criterion[0].split(' ')) == 1:
            ineq = filter_criterion[0].split(',')[0]
            value = float(filter_criterion[0].split(',')[1])
            data = []
            with open(path, 'r') as f:
                reader = csv.DictReader(f)
                if ineq == '>':
                    for row in reader:
                        row_buy = row['Buy-in Per Player'].split('$')
                        row_buy_int = float(row_buy[1])
                        
                        if row_buy_int > value:
                            data.append(row)

                if ineq == '<':
                    for row in reader:
                        row_buy = row['Buy-in Per Player'].split('$')
                        row_buy_int = float(row_buy[1])
                        
                        if row_buy_int < value:
                                data.append(row)

            with open(output_path, 'w', newline='') as fw:
                writer = csv.DictWriter(fw, fieldnames=header)
                writer.writeheader()
                for d in data: 
                    writer.writerow(d)

            print("Filtered by buy-in file created.")


    # platforms looks for either:
    # (1) console only --> xbox OR playstation
    # (2) pc only --> battlenet OR steam
    # (3) all --> anything else
    # expected input for 'filter_criterion' is a list
    if filter_category == "platforms":
        data = []
        with open(path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row_plat = row['Platforms']
                # row_plat = "['playstation']"
                # print(row_plat.__contains__('xbox'))
                if filter_criterion[0] == "console only": 
                    if (row_plat.__contains__('xbox') or row_plat.__contains__('playstation')) and not(row_plat.__contains__('battle.net')) and not(row_plat.__contains__('steam')):
                        data.append(row)
                    
                if filter_criterion[0] == "pc only": 
                    if (row_plat.__contains__('battle.net') or row_plat.__contains__('steam')) and not(row_plat.__contains__('xbox')) and not(row_plat.__contains__('playstation')):
                        data.append(row)

                if filter_criterion[0] == "all": 
                    if (row_plat.__contains__('battle.net') or row_plat.__contains__('steam')) and row_plat.__contains__('xbox') and row_plat.__contains__('playstation'):
                        data.append(row)
                        
        with open(output_path, 'w', newline='') as fw:
            writer = csv.DictWriter(fw, fieldnames=header)
            writer.writeheader()
            for d in data: 
                writer.writerow(d)

        print("Filtered by platform file created.")

    # team size looks for:
    # (1) team size --> 1v1, 2v2, 3v3, 4v4, 5v5, 6v6
    # expected input for 'filter_criterion' is a list
    if filter_category == "team size":
        data = []
        with open(path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row_value = int(row['Team Size'])
                if filter_criterion[0] == "1v1":
                    if row_value == 1:
                        data.append(row)

                if filter_criterion[0] == "2v2":
                    if row_value == 2:
                        data.append(row)

                if filter_criterion[0] == "3v3":
                    if row_value == 3:
                        data.append(row)

                if filter_criterion[0] == "4v4":
                  if row_value == 4:
                      data.append(row)

                if filter_criterion[0] == "5v5":
                  if row_value == 5:
                      data.append(row)

                if filter_criterion[0] == "6v6":
                    if row_value == 6:
                        data.append(row)

        with open(output_path, 'w', newline='') as fw:
            writer = csv.DictWriter(fw, fieldnames=header)
            writer.writeheader()
            for d in data: 
                writer.writerow(d)

        print("Filtered by team size file created.")


    # elimination type looks for:
    # (1) type of elimination --> single, double
    # expected input for 'filter_criterion' is a list
    if filter_category == "elimination type":
        data = []
        with open(path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row_value = row['Tournament Type (Ex: Single Elimination)']

                if filter_criterion[0] == "single":    
                    if row_value == "single elimination":
                        data.append(row)

                if filter_criterion[0] == "double":
                    if row_value == "double elimination":
                        data.append(row)
        
        with open(output_path, 'w', newline='') as fw:
            writer = csv.DictWriter(fw, fieldnames=header)
            writer.writeheader()
            for d in data: 
                writer.writerow(d)

        print("Filtered by elimination type file created.")


    # number of teams looks for:
    # (1) a threshold amount --> Ex: '>,5' or '<,5' format: '<greater than or less than>,<value>'
    # expected input for 'filter_criterion' is a list
    if filter_category == "number of teams":
        if len(filter_criterion[0].split(' ')) == 1:
            ineq = filter_criterion[0].split(',')[0]
            value = float(filter_criterion[0].split(',')[1])
            data = []
            with open(path, 'r') as f:
                reader = csv.DictReader(f)
                if ineq == '>':
                    for row in reader:
                        row_teams = row['Number of Teams Registered']
                        row_teams_int = float(row_teams)
                        
                        if row_teams_int > value:
                            data.append(row)

                if ineq == '<':
                    for row in reader:
                        row_teams = row['Number of Teams Registered']
                        row_teams_int = float(row_teams)
                        
                        if row_teams_int < value:
                                data.append(row)

            with open(output_path, 'w', newline='') as fw:
                writer = csv.DictWriter(fw, fieldnames=header)
                writer.writeheader()
                for d in data: 
                    writer.writerow(d)

            print("Filtered by number of teams file created.")


    # series type looks for:
    # (1) series type --> bo1, bo2, bo3 
    # expected input for 'filter_criterion' is a list
    if filter_category == "series type":
        data = []
        with open(path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row_value = row['Series Type (Ex: Best of 3)']

                if filter_criterion[0] == "bo1":    
                    if row_value == "Best of 1":
                        data.append(row)

                if filter_criterion[0] == "bo3":    
                    if row_value == "Best of 3":
                        data.append(row)

                if filter_criterion[0] == "bo5":    
                    if row_value == "Best of 5":
                        data.append(row)
        
        with open(output_path, 'w', newline='') as fw:
            writer = csv.DictWriter(fw, fieldnames=header)
            writer.writeheader()
            for d in data: 
                writer.writerow(d)

        print("Filtered by series type file created.")


    # prize looks for:
    # (1) a threshold amount --> Ex: '>,5' or '<,5' format: '<greater than or less than>,<value>'
    # expected input for 'filter_criterion' is a list
    if filter_category == "prize":
        if len(filter_criterion[0].split(' ')) == 1:
            ineq = filter_criterion[0].split(',')[0]
            value = float(filter_criterion[0].split(',')[1])
            data = []
            with open(path, 'r') as f:
                reader = csv.DictReader(f)
                if ineq == '>':
                    for row in reader:
                        row_prize = row['Prize Pool'].split('$')
                        row_prize_int = float(row_prize[1])
                        
                        if row_prize_int > value:
                            data.append(row)

                if ineq == '<':
                    for row in reader:
                        row_prize = row['Prize Pool'].split('$')
                        row_prize_int = float(row_prize[1])
                        
                        if row_prize_int < value:
                                data.append(row)

            with open(output_path, 'w', newline='') as fw:
                writer = csv.DictWriter(fw, fieldnames=header)
                writer.writeheader()
                for d in data: 
                    writer.writerow(d)

            print("Filtered by prize pool file created.")


    return None

# FOR TEST
# filter_write('series type', ['bo5'], output_path='filtered_by_series_type.csv')
