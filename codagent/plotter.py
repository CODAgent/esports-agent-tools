import csv
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt


# Inputs: X parameter, Y parameter, Input file to read from
# Returns: None
# Plots a graph of X vs Y
def plotter(x_param, y_param, input_file='all_data.csv'):
    with open(input_file, 'r') as fr:
        data = []
        reader = csv.reader(fr)
        
        for line in reader:
            data.append(line)

    # we probably always want to have time sorted data when plotting, so we need to sort by time
    # get rid of first line with the titles
    new_data = data[1:len(data)]
    new_data.sort(key=lambda date: datetime.strptime(date[0] + date[1], '%B %d, %Y' +  '%I:%M %p'))

    x_list

    y_list


plotter('asdf', 'asdf')
