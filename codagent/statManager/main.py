# imports 
import sys
import os
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter.filedialog import askopenfilename
tk.Tk().withdraw()

from processStats import processStats

# ---

# main function 
def main():
    # allow the user to choose the log file
    print('Please choose a "Data Log" file.')
    userInputFile = askopenfilename()
    try:
        # process stats and output the files to 'outputFiles'
        processStatsStatus = processStats(userInputFile)
    except FileNotFoundError:
        print('Please select a valid file.')
    return

# --- 
if __name__ == '__main__':
    args = sys.argv[1:len(sys.argv)]

    main()
