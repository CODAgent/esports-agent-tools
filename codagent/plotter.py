import csv
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt


# Inputs: X parameter, Y parameter, Input file to read from
# Returns: None
# Plots a graph of X vs Y
def plotter(x_param, y_param, input_file='all_data.csv', save_plot=False, output_file='plot.svg'):
    with open(input_file, 'r') as fr:
        data = []
        reader = csv.reader(fr)
        
        for line in reader:
            data.append(line)

    # we probably always want to have time sorted data when plotting, so we need to sort by time
    # get rid of first line with the titles
    new_data = data[1:len(data)]
    new_data.sort(key=lambda date: datetime.strptime(date[0] + date[1], '%B %d, %Y' +  '%I:%M %p'))

    # list of param keywords: time, buyin, platform, team_size,
    #                           elim, teams_entered, series, prize, profit
    # labels
    label_dict = {'time': 'Time (Time and Date)', 'buyin': 'Buy In Amount (USD)', 'platform': 'Platforms (Console Only, PC Only, All)', 'team_size': 'Team Size (Ex: 2v2)', 'elim': 'Elimination Type (Single or Double)', 'teams_entered': 'Number of Teams Entered', 'series': 'Series Type (Bo1, Bo3, Bo5)', 'prize': 'Prize (USD)', 'profit': 'Profit (USD)'}

    # X 
    x_list = []
    if x_param == 'time':
        for item in new_data:
            x_list.append(item[1] + ' on ' + item[0])

    elif x_param == 'buyin':
        for item in new_data:
            x_list.append(float(item[3].split('$')[1]))

    elif x_param == 'platform':
        # no battle net or steam --> console only
        # no xbox or playstation --> pc only
        # everything else --> all
        for item in new_data:
            if (item[4].find('battle.net') == -1) and (item[4].find('steam') == -1):
                x_list.append('console only')

            elif (item[4].find('xbox') == -1) and (item[4].find('playstation') == -1):
                x_list.append('pc only')

            else:
                x_list.append('all')

    elif x_param == 'team_size':
        for item in new_data:
            x_list.append(int(item[5]))

    elif x_param == 'elim':
        for item in new_data:
            x_list.append(item[6])

    elif x_param == 'teams_entered':
        for item in new_data:
            x_list.append(int(item[8]))

    elif x_param == 'series':
        for item in new_data:
            x_list.append(item[9])

    elif x_param == 'prize':
        for item in new_data:
            x_list.append(float(item[10].split('$')[1]))

    # TO BE IMPLEMENTED LATER
    # elif x_param == 'profit':

    else:
        print('Invalid x_param.')

    # Y 
    y_list = []
    if y_param == 'time':
        for item in new_data:
            y_list.append(item[1] + ' on ' + item[0])

    elif y_param == 'buyin':
        for item in new_data:
            y_list.append(float(item[3].split('$')[1]))

    elif y_param == 'platform':
        # no battle net or steam --> console only
        # no xbox or playstation --> pc only
        # everything else --> all
        for item in new_data:
            if (item[4].find('battle.net') == -1) and (item[4].find('steam') == -1):
                y_list.append('console only')

            elif (item[4].find('xbox') == -1) and (item[4].find('playstation') == -1):
                y_list.append('pc only')

            else:
                y_list.append('all')

    elif y_param == 'team_size':
        for item in new_data:
            y_list.append(int(item[5]))

    elif y_param == 'elim':
        for item in new_data:
            y_list.append(item[6])

    elif y_param == 'teams_entered':
        for item in new_data:
            y_list.append(int(item[8]))

    elif y_param == 'series':
        for item in new_data:
            y_list.append(item[9])

    elif y_param == 'prize':
        for item in new_data:
            y_list.append(float(item[10].split('$')[1]))

    # TO BE IMPLEMENTED LATER
    # elif y_param == 'profit':

    else:
        print('Invalid y_param.')

    # x_list

    # y_list
    fig = plt.figure(figsize=(16,9))
    plt.plot(x_list, y_list, '*-')
    plt.xlabel(label_dict[x_param], size=30)
    plt.ylabel(label_dict[y_param], size=30)
    plt.title(label_dict[y_param] + ' vs. ' + label_dict[x_param], size=35)
    if save_plot:
        plt.savefig(output_file)
    plt.show()


# plotter('time', 'teams_entered')
