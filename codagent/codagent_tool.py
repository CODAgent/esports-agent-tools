# GUI File for the CODAgent Analysis Tool

# imports
import os
import glob
import tkinter.messagebox
from tkinter import *
import main

curr_path = os.getcwd()

# init gui
title = 'CODAgent Analytics Tool'
win = Tk()
win.title('CODAgent Analytics Tool')
win.geometry('2400x1600')
win.config(bg='#94091F')
win.resizable(0, 0)

# grid configs
win.columnconfigure(0, weight=1)
win.columnconfigure(2, weight=1)
win.rowconfigure(0, weight=1)
win.rowconfigure(2, weight=1)

# create a frame
frame = Frame(win, bg='#FFFFFF')
frame.grid(row=1, column=1)


# ---
# banners
# logo = PhotoImage(file='') # add image=logo to title_banner
title_banner = Label(win, text='CODAgent Analytics Tool', foreground='#FFFFFF', background='#94091F', padx=10, pady=10, font=('Helvetica', 28), anchor='center')
title_banner.grid(row=0, column=0, columnspan=3, sticky='we')

author_banner = Label(win, text='Made by LonelyDock3', foreground='#FFFFFF', background='#94091F', padx=10, pady=10, font=('Helvetica', 20), anchor='center')
author_banner.grid(row=2, column=0, columnspan=3, sticky='we')

left_side = Label(win, background='#94091F')
left_side.grid(row=0, column=0, rowspan=3, sticky='ns')

right_side = Label(win, background='#94091F')
right_side.grid(row=0, column=2, rowspan=3, sticky='ns')
# ---


# using messagebox 
def hello():
    tkinter.messagebox.showinfo('hello')

# mine skeleton
def mine():
    mining = tkinter.messagebox.askyesno(title=title, message='Would you like to mine data?')
    if (mining):
        main.main(action='mine')
        tkinter.messagebox.showinfo(title=title, message='Mining Done (See terminal for results)')

# file selected function
def selected_file(file):
    return file

# return dropdown function
def dropdown_return(value):
    return value

# get all csv files available
csvs = glob.glob1(curr_path, '*.csv')

# filter button click
def filter_button():
    do_filter = tkinter.messagebox.askyesno(title=title, message='Would you like to filter the data you selected?')
    been_filtered = 0
    if (do_filter):
        # default filter
        filter_input_1 = 'date'
        filter_input_2 = ['September 22, 2022', 'September 22, 2022']

        ## 
        # format the data from the checked boxes here
        if date_checked.get():
            print('date')
            filter_input_1 = 'date'
            filter_input_2 = [start_date_string.get(), end_date_string.get()]
            been_filtered = 1

        if buyin_checked.get():
            print('buy')
            filter_input_1 = 'money'
            if buyin_variable.get() == 'Free Entry':
                filter_input_2 = ['free entry']
                been_filtered = 1

            elif buyin_variable.get() == 'Free Entry No Prize':
                filter_input_2 = ['free entry no prize']
                been_filtered = 1

            else:
                filter_input_2 = [buyin_variable.get() + ',' + buyin_string.get()]
                been_filtered = 1

        if platform_checked.get():
            print('plat')
            filter_input_1 = 'platforms'
            if platform_variable.get() == 'Console Only':
                filter_input_2 = ['console only']
                been_filtered = 1

            elif platform_variable.get() == 'PC Only':
                filter_input_2 = ['pc only']
                been_filtered = 1

            elif platform_variable.get() == 'All':
                filter_input_2 = ['all']
                been_filtered = 1

        if team_size_checked.get():
            print('team')
            filter_input_1 = 'team size'
            if team_size_variable.get() == '1v1':
                filter_input_2 = ['1v1']
                been_filtered = 1

            elif team_size_variable.get() == '2v2':
                filter_input_2 = ['2v2']
                been_filtered = 1

            elif team_size_variable.get() == '3v3':
                filter_input_2 = ['3v3']
                been_filtered = 1

            elif team_size_variable.get() == '4v4':
                filter_input_2 = ['4v4']
                been_filtered = 1

            elif team_size_variable.get() == '5v5':
                filter_input_2 = ['5v5']
                been_filtered = 1

            elif team_size_variable.get() == '6v6':
                filter_input_2 = ['6v6']
                been_filtered = 1

        if elim_checked.get():
            print('elim')
            filter_input_1 = 'elimination type'
            if elim_variable.get() == 'Single Elimination':
                filter_input_2 = ['single']
                been_filtered = 1
            elif elim_variable.get() == 'Double Elimination':
                filter_input_2 = ['double']
                been_filtered = 1

        if teams_entered_checked.get():
            print('entered')
            filter_input_1 = 'number of teams'
            filter_input_2 = [teams_entered_variable.get() + ',' + teams_entered_string.get()]
            been_filtered = 1

        if series_checked.get():
            print('series')
            filter_input_1 = 'series type'
            if series_variable.get() == 'Best of 1':
                filter_input_2 = ['bo1']
                been_filtered = 1

            elif series_variable.get() == 'Best of 3':
                filter_input_2 = ['bo3']
                been_filtered = 1

            elif series_variable.get() == 'Best of 5':
                filter_input_2 = ['bo5']
                been_filtered = 1

        if prize_checked.get():
            print('prize')
            filter_input_1 = 'prize'
            filter_input_2 = [prize_variable.get() + ',' + prize_string.get()]
            been_filtered = 1

        ##

        if variable.get():
            main_file = variable.get()
            no_input_file = 0
        else:
            no_input_file = 1
            been_filtered = 0

        if filter_output_string.get():
            check_str = filter_output_string.get().split('.')
            if len(check_str) < 2:
                no_output_file = 1
                been_filtered = 0
            else:
                if check_str[len(check_str)-1] != 'csv':
                    no_output_file = 1
                    been_filtered = 0
                else:
                    filter_output_file = filter_output_string.get()
                    no_output_file = 0
        else: 
            no_output_file = 1
            been_filtered = 0

        if been_filtered:
            main.main(action='filter', filter_input_1=filter_input_1, filter_input_2=filter_input_2, main_path=main_file, filter_path=filter_output_file)
            tkinter.messagebox.showinfo(title=title, message='Data has been filtered')      
        else: 
            if no_input_file:
                tkinter.messagebox.showinfo(title=title, message='Please select an input file for data to filter on at the bottom left (Ex: "all_data.csv").')      
            elif no_output_file:
                tkinter.messagebox.showinfo(title=title, message='Please specify a proper output file for the filtered data to be written to. (Type needs to be a CSV.  Ex: "filtered_data.csv").')      
            else:
                tkinter.messagebox.showinfo(title=title, message='No data was selected to be filtered or there was an error.')      


# stats button click
def stats_button():
    do_stats = tkinter.messagebox.askyesno(title=title, message='Would you like to calculate statistics on the data you selected?')
    if (do_stats):
        tkinter.messagebox.showinfo(title=title, message='Calculating stats')

# plot button click
def plot_button():
    do_plot = tkinter.messagebox.askyesno(title=title, message='Would you like to plot the data you selected?')
    if (do_plot):
        tkinter.messagebox.showinfo(title=title, message='Plotting data')

# general report button click
def report_button():
    do_report = tkinter.messagebox.askyesno(title=title, message='Would you like to generate the report?')
    if (do_report):
        tkinter.messagebox.showinfo(title=title, message='Making report')


# thought: for each action, make a popup that basically says "loading" until the 
# action is finished and then the popup closes and another popup appears with the
# status message
    
# ---
# mine button 
# btn = Button(frame, text='Mine Data', width=10, height=5, command=mine)
btn = Button(frame, text='Mine Data', command=mine, background='#4CBD2A', font=('Helvetica', 16))
btn.grid(row=0, column=0, columnspan=3, sticky='new')
# ---

# ---
# options section
options_frame = Frame(frame, bg='#FFFFFF', highlightbackground='#000000', highlightthickness=2)
options_frame.grid(row=1, column=0, sticky='wew')

options_title = Label(options_frame, text='Options', foreground='#000000', background='#FFFFFF', padx=5, pady=5, font=('Helvetica', 14), anchor='center')
options_title.grid(row=0, column=0, columnspan=2)


# Date
# will be 0 or 1 if the checkbox is checked
date_checked = IntVar()
date_checkbox = Checkbutton(options_frame, text='Date (Format: Month Date, Year)', variable=date_checked)
date_checkbox.grid(row=1, column=0, sticky='w')

start_date_title = Label(options_frame, text='Start Date (Spell out full month and year.  Capitalize first letter of month.)', padx=5, pady=5, anchor='center')
start_date_title.grid(row=2, column=0)

start_date_string = StringVar()
start_date_entry = Entry(options_frame, textvariable=start_date_string)
start_date_entry.grid(row=2, column=1)

end_date_title = Label(options_frame, text='End Date (Spell out full month and year.  Capitalize first letter of month.)', padx=5, pady=5, anchor='center')
end_date_title.grid(row=3, column=0)

end_date_string = StringVar()
end_date_entry = Entry(options_frame, textvariable=end_date_string)
end_date_entry.grid(row=3, column=1)


# Buy-in price 
buyin_checked = IntVar()
buyin_checkbox = Checkbutton(options_frame, text='Buy-in price', variable=buyin_checked)
buyin_checkbox.grid(row=4, column=0, sticky='w')

buyin_options = ['Free Entry', 'Free Entry No Prize', '>', '<']
buyin_variable = StringVar()
buyin_dropdown = OptionMenu(
    options_frame,              # frame to put the dropdown in
    buyin_variable,             # variable means the dropdown items can change
    *buyin_options,              # list within the dropdown
    command=dropdown_return     # the action the dropdown will do
)
buyin_dropdown.grid(row=5, column=0)

buyin_string = StringVar()
buyin_entry = Entry(options_frame, textvariable=buyin_string)
buyin_entry.grid(row=5, column=1)


# Platform
platform_checked = IntVar()
platform_checkbox = Checkbutton(options_frame, text='Platforms', variable=platform_checked)
platform_checkbox.grid(row=6, column=0, sticky='w')

platform_options = ['Console Only', 'PC Only', 'All']
platform_variable = StringVar()
platform_dropdown = OptionMenu(
    options_frame,              # frame to put the dropdown in
    platform_variable,             # variable means the dropdown items can change
    *platform_options,              # list within the dropdown
    command=dropdown_return     # the action the dropdown will do
)
platform_dropdown.grid(row=7, column=0)


# Team size
team_size_checked = IntVar()
team_size_checkbox = Checkbutton(options_frame, text='Team Size', variable=team_size_checked)
team_size_checkbox.grid(row=8, column=0, sticky='w')

team_size_options = ['1v1', '2v2', '3v3', '4v4', '5v5', '6v6']
team_size_variable = StringVar()
team_size_dropdown = OptionMenu(
    options_frame,              # frame to put the dropdown in
    team_size_variable,             # variable means the dropdown items can change
    *team_size_options,              # list within the dropdown
    command=dropdown_return     # the action the dropdown will do
)
team_size_dropdown.grid(row=9, column=0)


# Elimination type
elim_checked = IntVar()
elim_checkbox = Checkbutton(options_frame, text='Elimination Type', variable=elim_checked)
elim_checkbox.grid(row=10, column=0, sticky='w')

elim_options = ['Single Elimination', 'Double Elimination']
elim_variable = StringVar()
elim_dropdown = OptionMenu(
    options_frame,              # frame to put the dropdown in
    elim_variable,             # variable means the dropdown items can change
    *elim_options,              # list within the dropdown
    command=dropdown_return     # the action the dropdown will do
)
elim_dropdown.grid(row=11, column=0)


# Number of teams entered
teams_entered_checked = IntVar()
teams_entered_checkbox = Checkbutton(options_frame, text='Number of Teams Entered', variable=teams_entered_checked)
teams_entered_checkbox.grid(row=12, column=0, sticky='w')

teams_entered_options = ['>', '<']
teams_entered_variable = StringVar()
teams_entered_dropdown = OptionMenu(
    options_frame,              # frame to put the dropdown in
    teams_entered_variable,             # variable means the dropdown items can change
    *teams_entered_options,              # list within the dropdown
    command=dropdown_return     # the action the dropdown will do
)
teams_entered_dropdown.grid(row=13, column=0)

teams_entered_string = StringVar()
teams_entered_entry = Entry(options_frame, textvariable=teams_entered_string)
teams_entered_entry.grid(row=13, column=1)


# Series type
series_checked = IntVar()
series_checkbox = Checkbutton(options_frame, text='Series Type', variable=series_checked)
series_checkbox.grid(row=14, column=0, sticky='w')

series_options = ['Best of 1', 'Best of 3', 'Best of 5']
series_variable = StringVar()
series_dropdown = OptionMenu(
    options_frame,              # frame to put the dropdown in
    series_variable,             # variable means the dropdown items can change
    *series_options,              # list within the dropdown
    command=dropdown_return     # the action the dropdown will do
)
series_dropdown.grid(row=15, column=0)


# Prize pool
prize_checked = IntVar()
prize_checkbox = Checkbutton(options_frame, text='Prize Pool', variable=prize_checked)
prize_checkbox.grid(row=16, column=0, sticky='w')

prize_options = ['>', '<']
prize_variable = StringVar()
prize_dropdown = OptionMenu(
    options_frame,              # frame to put the dropdown in
    prize_variable,             # variable means the dropdown items can change
    *prize_options,              # list within the dropdown
    command=dropdown_return     # the action the dropdown will do
)
prize_dropdown.grid(row=17, column=0)

prize_string = StringVar()
prize_entry = Entry(options_frame, textvariable=prize_string)
prize_entry.grid(row=17, column=1)


# Input file drop down
input_file_title = Label(options_frame, text='Input File', foreground='#000000', background='#FFFFFF', padx=5, pady=5, font=('Helvetica', 12), anchor='center')
input_file_title.grid(row=18, column=0)
variable = StringVar()
input_file_dropdown = OptionMenu(
    options_frame,              # frame to put the dropdown in
    variable,                   # variable means the dropdown items can change
    *csvs,                      # list within the dropdown
    command=selected_file       # the action the dropdown will do
)
input_file_dropdown.grid(row=19, column=0, sticky='we')

# ---



# ---
# actions section
# btn = Button(frame, text='Actions place holder', command=mine)
# btn.grid(row=1, column=1, rowspan=5)
actions_frame = Frame(frame, bg='#FFFFFF', highlightbackground='#000000', highlightthickness=2)
actions_frame.grid(row=1, column=1, sticky='ew')

actions_title = Label(actions_frame, text='Actions', foreground='#000000', background='#FFFFFF', padx=5, pady=5, font=('Helvetica', 14), anchor='center')
actions_title.grid(row=0, column=0, columnspan=2)

p1 = Label(actions_frame, text='Place Holder', foreground='#FFFFFF', background='#FFFFFF', padx=5, pady=5, font=('Helvetica', 14), anchor='center')
p1.grid(row=1, column=0, columnspan=2)


# filter
# need a dropdown to select input file 
# need an entry to name the output file (if no .csv, then add .csv)
# maybe use some recursive thing if there's multiple checkboxes selected? --> don't do this at first
filter_btn = Button(actions_frame, text='Filter Data', command=filter_button, background='#DBEE66', font=('Helvetica', 16))
filter_btn.grid(row=2, column=0, columnspan=2, sticky='ew')

filter_output_title = Label(actions_frame, text='Output File Name (with ".csv" at the end)', foreground='#000000', background='#FFFFFF', padx=5, pady=5, font=('Helvetica', 12), anchor='center')
filter_output_title.grid(row=3, column=0, columnspan=1)

filter_output_string = StringVar()
filter_output_entry = Entry(actions_frame, textvariable=filter_output_string)
filter_output_entry.grid(row=3, column=1, columnspan=1)

p2 = Label(actions_frame, text='Place Holder', foreground='#FFFFFF', background='#FFFFFF', padx=5, pady=5, font=('Helvetica', 14), anchor='center')
p2.grid(row=4, column=0, columnspan=2)


# plot
# support 2D (for now)
# specify with a dropdown which checked box is X and which is Y
plot_btn = Button(actions_frame, text='Plot Data (X, Y)', command=plot_button, background='#283FEB', font=('Helvetica', 16))
plot_btn.grid(row=5, column=0, columnspan=2, sticky='ew')

plot_x_title = Label(actions_frame, text='X Variable:', foreground='#000000', background='#FFFFFF', padx=5, pady=5, font=('Helvetica', 12), anchor='center')
plot_x_title.grid(row=6, column=0, columnspan=1)

plot_x_variable = StringVar()
plot_x_list = ['logic needed here']
plot_x_dropdown =  OptionMenu(
    actions_frame,              # frame to put the dropdown in
    plot_x_variable,                   # variable means the dropdown items can change
    *plot_x_list,                      # list within the dropdown
    command=selected_file       # the action the dropdown will do
)
plot_x_dropdown.grid(row=6, column=1, sticky='ew')

plot_y_title = Label(actions_frame, text='Y Variable:', foreground='#000000', background='#FFFFFF', padx=5, pady=5, font=('Helvetica', 12), anchor='center')
plot_y_title.grid(row=7, column=0, columnspan=1)

plot_y_variable = StringVar()
plot_y_list = ['logic needed here']
plot_y_dropdown =  OptionMenu(
    actions_frame,              # frame to put the dropdown in
    plot_y_variable,                   # variable means the dropdown items can change
    *plot_y_list,                      # list within the dropdown
    command=selected_file       # the action the dropdown will do
)
plot_y_dropdown.grid(row=7, column=1, sticky='ew')

p3 = Label(actions_frame, text='Place Holder', foreground='#FFFFFF', background='#FFFFFF', padx=5, pady=5, font=('Helvetica', 14), anchor='center')
p3.grid(row=8, column=0, columnspan=2)


# calculate
# specify with a dropdown what operation should be performed (mean, median, mode, max, min, total)
stats_btn = Button(actions_frame, text='Calculate Stats', command=stats_button, background='#EB8628', font=('Helvetica', 16))
stats_btn.grid(row=9, column=0, columnspan=2, sticky='ew')

stats_title = Label(actions_frame, text='Stat to calculate:', foreground='#000000', background='#FFFFFF', padx=5, pady=5, font=('Helvetica', 12), anchor='center')
stats_title.grid(row=10, column=0, columnspan=1)

stats_variable = StringVar()
stats_list = ['mean', 'median', 'mode', 'max', 'min', 'total']
stats_dropdown =  OptionMenu(
    actions_frame,              # frame to put the dropdown in
    stats_variable,                   # variable means the dropdown items can change
    *stats_list,                      # list within the dropdown
    command=selected_file       # the action the dropdown will do
)
stats_dropdown.grid(row=10, column=1, sticky='ew')

p4 = Label(actions_frame, text='Place Holder', foreground='#FFFFFF', background='#FFFFFF', padx=5, pady=5, font=('Helvetica', 14), anchor='center')
p4.grid(row=11, column=0, columnspan=2)


# report
report_btn = Button(actions_frame, text='General Report', command=report_button, background='#0FF1E9', font=('Helvetica', 16))
report_btn.grid(row=12, column=0, columnspan=2, sticky='ew')

p5 = Label(actions_frame, text='Place Holder', foreground='#FFFFFF', background='#FFFFFF', padx=5, pady=5, font=('Helvetica', 14), anchor='center')
p5.grid(row=13, column=0, columnspan=2)



# ---


# ---
# actions help section
# btn = Button(frame, text='Actions Help place holder', command=mine)
# btn.grid(row=1, column=2, rowspan=5)
actions_help_frame = Frame(frame, bg='#FFFFFF', highlightbackground='#000000', highlightthickness=2)
actions_help_frame.grid(row=1, column=2, sticky='eew')

actions_help_title = Label(actions_help_frame, text='Actions Help', foreground='#000000', background='#FFFFFF', padx=5, pady=5, font=('Helvetica', 14), anchor='center')
actions_help_title.grid(row=0, column=0)
# ---


# ---
win.mainloop()
