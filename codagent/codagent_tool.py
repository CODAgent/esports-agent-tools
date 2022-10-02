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


# using messagebox 
def hello():
    tkinter.messagebox.showinfo('hello')

# mine skeleton
def mine():
    tkinter.messagebox.showinfo(title=title, message='Mining data')



# thought: for each action, make a popup that basically says "loading" until the 
# action is finished and then the popup closes and another popup appears with the
# status message
    
# mine button 
btn = Button(frame, text='Mine Data', width=10, height=5, command=mine)
btn.grid(row=0, columnspan=3, sticky='n')

# options section


# actions section


# actions help section


win.mainloop()
