# GUI File for the CODAgent Analysis Tool

# imports
import tkinter.messagebox
from tkinter import *

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
options_title.grid(row=0, column=0)
# ---



# ---
# actions section
# btn = Button(frame, text='Actions place holder', command=mine)
# btn.grid(row=1, column=1, rowspan=5)
actions_frame = Frame(frame, bg='#FFFFFF', highlightbackground='#000000', highlightthickness=2)
actions_frame.grid(row=1, column=1, sticky='ew')
actions_title = Label(actions_frame, text='Actions', foreground='#000000', background='#FFFFFF', padx=5, pady=5, font=('Helvetica', 14), anchor='center')
actions_title.grid(row=0, column=0)
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
