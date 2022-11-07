# GUI File for the CODAgent Analysis Tool

# imports
import os
import glob
import tkinter.messagebox
from tkinter import *

curr_path = os.getcwd()

# init gui
title = 'CODAgent Analytics Tool'
win = Tk()
win.title('CODAgent Analytics Tool')
win.geometry('1600x1600')
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
    tkinter.messagebox.showinfo(title=title, message='Mining data')

# file selected function
def selected_file(file):
    return file

# return dropdown function
def dropdown_return(value):
    return value

# get all csv files available
csvs = glob.glob1(curr_path, '*.csv')



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
end_date_title = Label(options_frame, text='Start Date', padx=5, pady=5, anchor='center')
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
variable = StringVar()
input_file_dropdown = OptionMenu(
    options_frame,              # frame to put the dropdown in
    variable,                   # variable means the dropdown items can change
    *csvs,                      # list within the dropdown
    command=selected_file       # the action the dropdown will do
)
input_file_dropdown.grid(row=18, column=0, sticky='we')

# ---



# ---
# actions section
# btn = Button(frame, text='Actions place holder', command=mine)
# btn.grid(row=1, column=1, rowspan=5)
actions_frame = Frame(frame, bg='#FFFFFF', highlightbackground='#000000', highlightthickness=2)
actions_frame.grid(row=1, column=1, sticky='ew')
actions_title = Label(actions_frame, text='Actions', foreground='#000000', background='#FFFFFF', padx=5, pady=5, font=('Helvetica', 14), anchor='center')
actions_title.grid(row=0, column=0)

# filter
# need a dropdown to select input file 
# need an entry to name the output file (if no .csv, then add .csv)
# maybe use some recursive thing if there's multiple checkboxes selected? --> don't do this at first


# plot
# support 2D (for now)
# specify with a dropdown which checked box is X and which is Y


# calculate
# specify with a dropdown what operation should be performed (mean, median, mode, max, min, total)


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
