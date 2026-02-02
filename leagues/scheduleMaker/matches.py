#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  7 16:16:08 2025

@author: Kevin Rotz
"""

# imports
import os
import tkinter as tk
from tkinter import filedialog
import numpy as np
import pandas as pd
import scipy as sp
from scipy import optimize
import matplotlib.pyplot as plt

# function: readInInputCsv - collect team names, total weeks, and matches per week
#   - For now this function assumes that the input CSV has the first column as the team names, the second column as the total weeks with one rows worth of data, and the third column as matches per week with one rows worth of data
# input:
#   - inputCsvPath
# outputs:
#   - teamList
#   - totalWeeks
#   - matchesPerWeek
def readInInputCsv(inputCsvPath):
    teamList = []
    totalWeeks = 0
    matchesPerWeek = 0

    with open(inputCsvPath, 'r') as fr:
        lines = fr.readlines()
    
    for lineIdx, line in enumerate(lines):
        lineSplit = line.split(',')

        # header
        if lineIdx == 0:
            continue
        elif lineIdx == 1:
            totalWeeks = int(lineSplit[1])
            matchesPerWeek = int(lineSplit[2])

        teamList.append(lineSplit[0])


    return teamList, totalWeeks, matchesPerWeek

# function: generateMatches - Used to create all of the matches
# inputs:
#   - totalWeeks
#   - matchesPerWeek 
#   - teamList: List of the teams
#   - visualize: Boolean to show plots or not
# output:
#   - Dictionary of all the matches for each week
def generateMatches(totalWeeks, matchesPerWeek, teamList, visualize=False):
    W = totalWeeks
    M = matchesPerWeek
    teams = teamList
    T = len(teams)

    outputDict = {'week': [], 'awayTeam': [], 'homeTeam': []}

    # cumulative number of times each team plays
    xtot = np.zeros((T,T))

    # cost vector
    c  = np.zeros((T,T))

    # Make cost of a team playing itself so large as to make it infeasible
    for ii in range(T):
        c[ii,ii] = 1e6

    A = np.zeros((0,T*T))
    b = np.array([])

    # Constraints that each team play M matches per week
    for ii in range(T):
        r = np.zeros((T,T))
        r[:,ii] = 1
        r[ii,ii] = 0 # a team playing itself doesn't count
        r = r.ravel()
        A = np.vstack([A,r])
        b   = np.append(b,M)


    # Constraint that if team i plays team j, then team j plays team i
    for ii in range(T):
        for jj in range(ii+1,T):
            r = np.zeros((T,T))
            r[ii,jj] = 1
            r[jj,ii] = -1
            r = r.ravel()
            A = np.vstack([A,r])
            b   = np.append(b,0)

    # collect the matches
    for ww in range(W):        
        sol = sp.optimize.linprog(c.ravel(), 
                                  A_eq = A, b_eq = b, 
                                  bounds = (0,1), 
                                  integrality = 1)

        assert sol.success, 'Solver failed. You may need more teams to be able to play this many weekly matches'

        x = sol.x.reshape((T,T))

        assert np.array_equal(x,x.T), "non-reciprocating match"

        xtot += x
        for ii in range(T):
            for jj in range(ii,T):
                if x[ii,jj] == 1:

                    assert ii != jj , 'A team is scheduled to play itself, something is wrong (probably bad constraints)'
                    # alternate away @ home
                    if xtot[ii,jj] % 2 == 1:
                        outputDict['week'].append(ww + 1)
                        outputDict['awayTeam'].append(teams[ii])
                        outputDict['homeTeam'].append(teams[jj])
                    else:
                        outputDict['week'].append(ww + 1)
                        outputDict['awayTeam'].append(teams[jj])
                        outputDict['homeTeam'].append(teams[ii])

                    # increase the cost of playing again by M + 1
                    c[ii,jj] += M + 1
                    c[jj,ii] += M + 1

    if visualize:
        """ 
        plot the results. looking for the max number of matches and the min number of 
        matches to be within 1 of each other. Also expecting no team to play itself 
        """
        plt.close('all')        
        plt.figure()
        plt.imshow(xtot)
        plt.title('total number of matches across the season')
        plt.colorbar()
        plt.show()
    
    return outputDict

# function: writeOutputCsv - write the contents of outputDict to a CSV file
# inputs:
#   - outputDict - result from generateMatches
#   - outputDir - directory the output file will be written to
# output:
#   - Output file written to the output directory
def writeOutputCsv(outputDict, outputDir):
    outputFilePath = os.path.join(outputDir, 'outputFile.csv')
    outputDf = pd.DataFrame(outputDict)
    outputDf.to_csv(outputFilePath, index=False, encoding='utf-8')

    print('File written to: ' + outputFilePath)
    return

def main():
    # get inputs
    root = tk.Tk()
    root.withdraw()
    currDir = os.getcwd()
    print('Select an input CSV file')
    inputFilePath = filedialog.askopenfilename(title="Select an input CSV file", filetypes=[("CSV files", "*.csv")], initialdir=currDir)

    print('Select an output CSV file')
    outputDirPath = filedialog.askdirectory(title="Select an output directory", initialdir=currDir)

    print(inputFilePath)
    print(outputDirPath)

    # error handling
    errorList = []
    if not(os.path.isfile(inputFilePath)):
        errorList.append('Invalid input file path.')
    if not(os.path.isdir(outputDirPath)):
        errorList.append('Invalid output file path.')
    
    if 0 < len(errorList):
        for error in errorList:
            print(error)
        return

    # run functionality
    teamList, totalWeeks, matchesPerWeek = readInInputCsv(inputFilePath)
    outputDict = generateMatches(totalWeeks, matchesPerWeek, teamList)

    # write outputs
    writeOutputCsv(outputDict, outputDirPath)

    return

if __name__ == "__main__":
    main()