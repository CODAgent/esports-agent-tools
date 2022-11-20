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
    tkinter.messagebox.showinfo(title=title, message='Filtering data')

# stats button click
def stats_button():
    tkinter.messagebox.showinfo(title=title, message='Calculating stats')

# plot button click
def plot_button():
    tkinter.messagebox.showinfo(title=title, message='Plotting data')

# general report button click
def report_button():
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
date_checkbox = Checkbutton(options_frame, text='Date (Format: MM-DD-YYYY)')
date_checkbox.grid(row=1, column=0, sticky='w')

start_date_title = Label(options_frame, text='Start Date', padx=5, pady=5, anchor='center')
start_date_title.grid(row=2, column=0)
start_date_entry = Entry(options_frame)
start_date_entry.grid(row=2, column=1)
end_date_title = Label(options_frame, text='End Date', padx=5, pady=5, anchor='center')
end_date_title.grid(row=3, column=0)
end_date_entry = Entry(options_frame)
end_date_entry.grid(row=3, column=1)

# Buy-in price 
buyin_checkbox = Checkbutton(options_frame, text='Buy-in price')
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
buyin_entry = Entry(options_frame)
buyin_entry.grid(row=5, column=1)

# Platform
platform_checkbox = Checkbutton(options_frame, text='Platforms')
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
team_size_checkbox = Checkbutton(options_frame, text='Team Size')
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
elim_checkbox = Checkbutton(options_frame, text='Elimination Type')
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
teams_entered_checkbox = Checkbutton(options_frame, text='Number of Teams Entered')
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
teams_entered_entry = Entry(options_frame)
teams_entered_entry.grid(row=13, column=1)

# Series type
series_checkbox = Checkbutton(options_frame, text='Series Type')
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
prize_checkbox = Checkbutton(options_frame, text='Prize Pool')
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
prize_entry = Entry(options_frame)
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
filter_input_title = Label(actions_frame, text='Input File', foreground='#000000', background='#FFFFFF', padx=5, pady=5, font=('Helvetica', 12), anchor='center')
filter_input_title.grid(row=3, column=0, columnspan=1)
filter_variable = StringVar()
filter_dropdown =  OptionMenu(
    actions_frame,              # frame to put the dropdown in
    filter_variable,                   # variable means the dropdown items can change
    *csvs,                      # list within the dropdown
    command=selected_file       # the action the dropdown will do
)
filter_dropdown.grid(row=3, column=1, sticky='ew')
filter_output_title = Label(actions_frame, text='Output File Name (with ".csv" at the end)', foreground='#000000', background='#FFFFFF', padx=5, pady=5, font=('Helvetica', 12), anchor='center')
filter_output_title.grid(row=4, column=0, columnspan=1)
filter_output_entry = Entry(actions_frame)
filter_output_entry.grid(row=4, column=1, columnspan=1)
p2 = Label(actions_frame, text='Place Holder', foreground='#FFFFFF', background='#FFFFFF', padx=5, pady=5, font=('Helvetica', 14), anchor='center')
p2.grid(row=5, column=0, columnspan=2)


# plot
# support 2D (for now)
# specify with a dropdown which checked box is X and which is Y
plot_btn = Button(actions_frame, text='Plot Data (X, Y)', command=plot_button, background='#283FEB', font=('Helvetica', 16))
plot_btn.grid(row=6, column=0, columnspan=2, sticky='ew')
plot_x_title = Label(actions_frame, text='X Variable:', foreground='#000000', background='#FFFFFF', padx=5, pady=5, font=('Helvetica', 12), anchor='center')
plot_x_title.grid(row=7, column=0, columnspan=1)
plot_x_variable = StringVar()
plot_x_list = ['logic needed here']
plot_x_dropdown =  OptionMenu(
    actions_frame,              # frame to put the dropdown in
    plot_x_variable,                   # variable means the dropdown items can change
    *plot_x_list,                      # list within the dropdown
    command=selected_file       # the action the dropdown will do
)
plot_x_dropdown.grid(row=7, column=1, sticky='ew')
plot_y_title = Label(actions_frame, text='Y Variable:', foreground='#000000', background='#FFFFFF', padx=5, pady=5, font=('Helvetica', 12), anchor='center')
plot_y_title.grid(row=8, column=0, columnspan=1)
plot_y_variable = StringVar()
plot_y_list = ['logic needed here']
plot_y_dropdown =  OptionMenu(
    actions_frame,              # frame to put the dropdown in
    plot_y_variable,                   # variable means the dropdown items can change
    *plot_y_list,                      # list within the dropdown
    command=selected_file       # the action the dropdown will do
)
plot_y_dropdown.grid(row=8, column=1, sticky='ew')
p3 = Label(actions_frame, text='Place Holder', foreground='#FFFFFF', background='#FFFFFF', padx=5, pady=5, font=('Helvetica', 14), anchor='center')
p3.grid(row=9, column=0, columnspan=2)


# calculate
# specify with a dropdown what operation should be performed (mean, median, mode, max, min, total)
stats_btn = Button(actions_frame, text='Calculate Stats', command=stats_button, background='#EB8628', font=('Helvetica', 16))
stats_btn.grid(row=10, column=0, columnspan=2, sticky='ew')
stats_title = Label(actions_frame, text='Stat to calculate:', foreground='#000000', background='#FFFFFF', padx=5, pady=5, font=('Helvetica', 12), anchor='center')
stats_title.grid(row=11, column=0, columnspan=1)
stats_variable = StringVar()
stats_list = ['mean', 'median', 'mode', 'max', 'min', 'total']
stats_dropdown =  OptionMenu(
    actions_frame,              # frame to put the dropdown in
    stats_variable,                   # variable means the dropdown items can change
    *stats_list,                      # list within the dropdown
    command=selected_file       # the action the dropdown will do
)
stats_dropdown.grid(row=11, column=1, sticky='ew')
p4 = Label(actions_frame, text='Place Holder', foreground='#FFFFFF', background='#FFFFFF', padx=5, pady=5, font=('Helvetica', 14), anchor='center')
p4.grid(row=12, column=0, columnspan=2)

# report
report_btn = Button(actions_frame, text='General Report', command=report_button, background='#0FF1E9', font=('Helvetica', 16))
report_btn.grid(row=13, column=0, columnspan=2, sticky='ew')
p5 = Label(actions_frame, text='Place Holder', foreground='#FFFFFF', background='#FFFFFF', padx=5, pady=5, font=('Helvetica', 14), anchor='center')
p5.grid(row=14, column=0, columnspan=2)



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
