# imports 
import os
import numpy as np
import pandas as pd

# ---

# Inputs:
# Outputs:
#   The function will output CSV files to the 'outputFiles' directory
#   The function will return a success flag, which is equal to 1 if there were no errors or 0 if there was at least one error 
def processStats(logFilePath):
    success = 0

    # read in the csv
    lines = []
    with open(logFilePath, 'r') as fr:
        lines = fr.readlines()

    # [0] date, [1] player, [2] game mode, [3] map, [4] kills, [5] deaths, [6] damage, [7] objMainStat
    header = lines[0]
    linesOfInterest = lines[1:len(lines)]

    dataDict = {'date': [], 'player': [], 'gameMode': [], 'map': [], 'opponent': [], 'kills': [], 'deaths': [], 'damage': [], 'objMainStat': []}
    objMainStatMap = {'Hardpoint': 'hillTime', 'SND': 'firstBloods', 'Control': 'ticks'}

    for lineIdx, line in enumerate(linesOfInterest):
        currLine = line.strip('\n')
        currLineSplit = currLine.split(',')

        dataDict['date'].append(currLineSplit[0])
        dataDict['player'].append(currLineSplit[1])
        dataDict['gameMode'].append(currLineSplit[2])
        dataDict['map'].append(currLineSplit[3])
        dataDict['opponent'].append(currLineSplit[4])
        dataDict['kills'].append(currLineSplit[5])
        dataDict['deaths'].append(currLineSplit[6])
        dataDict['damage'].append(currLineSplit[7])
        dataDict['objMainStat'].append(currLineSplit[8])

    dataDfTmp = pd.DataFrame(dataDict)
    dataDf = dataDfTmp.apply(pd.to_numeric, errors='coerce').fillna(dataDfTmp)

    allPlayers = dataDf['player'].unique()
    allDates = dataDf['date'].unique()
    allMaps = dataDf['map'].unique()

    # player
    playerGrouped = dataDf.groupby('player')
    playerTotals = playerGrouped.sum(numeric_only=True)
    playerTotals['kdRatio'] = playerTotals.loc[:, 'kills'] / playerTotals.loc[:, 'deaths']
    playerAvgs = playerGrouped.mean(numeric_only=True)

    # player gamemode 
    playerGamemodeGrouped = dataDf.groupby(['player', 'gameMode'])
    playerGamemodeTotals = playerGamemodeGrouped.sum(numeric_only=True)
    playerGamemodeTotals['kdRatio'] = playerGamemodeTotals.loc[:, 'kills'] / playerGamemodeTotals.loc[:, 'deaths']
    playerGamemodeAvgs = playerGamemodeGrouped.mean(numeric_only=True)

    # player map
    playerMapGrouped = dataDf.groupby(['player', 'map'])
    playerMapTotals = playerMapGrouped.sum(numeric_only=True)
    playerMapTotals['kdRatio'] = playerMapTotals.loc[:, 'kills'] / playerMapTotals.loc[:, 'deaths']
    playerMapAvgs = playerMapGrouped.mean(numeric_only=True)

    # player map gamemode 
    playerMapGamemodeGrouped = dataDf.groupby(['player', 'map', 'gameMode'])
    playerMapGamemodeTotals = playerMapGamemodeGrouped.sum(numeric_only=True)
    playerMapGamemodeTotals['kdRatio'] = playerMapGamemodeTotals.loc[:, 'kills'] / playerMapGamemodeTotals.loc[:, 'deaths']
    playerMapGamemodeAvgs = playerMapGamemodeGrouped.mean(numeric_only=True)


    # outputting 
    outputDir = 'outputFiles'

    # total outputs 
    playerTotalOutputFile = 'playerTotals.csv'
    playerGamemodeTotalOutputFile = 'playerGamemodeTotals.csv'
    playerMapTotalOutputFile = 'playerMapTotals.csv'
    playerMapGamemodeTotalOutputFile = 'playerMapGamemodeTotals.csv'

    playerTotals.to_csv(os.path.join(outputDir, playerTotalOutputFile))
    playerGamemodeTotals.to_csv(os.path.join(outputDir, playerGamemodeTotalOutputFile))
    playerMapTotals.to_csv(os.path.join(outputDir, playerMapTotalOutputFile))
    playerMapGamemodeTotals.to_csv(os.path.join(outputDir, playerMapGamemodeTotalOutputFile))

    print(os.path.join(outputDir, playerTotalOutputFile))
    print(os.path.join(outputDir, playerGamemodeTotalOutputFile))
    print(os.path.join(outputDir, playerMapTotalOutputFile))
    print(os.path.join(outputDir, playerMapGamemodeTotalOutputFile))

    # avg outputs
    playerAvgOutputFile = 'playerAvgs.csv'
    playerGamemodeAvgOutputFile = 'playerGamemodeAvgs.csv'
    playerMapAvgOutputFile = 'playerMapAvgs.csv'
    playerMapGamemodeAvgOutputFile = 'playerMapGamemodeAvgs.csv'

    playerAvgs.to_csv(os.path.join(outputDir, playerAvgOutputFile))
    playerGamemodeAvgs.to_csv(os.path.join(outputDir, playerGamemodeAvgOutputFile))
    playerMapAvgs.to_csv(os.path.join(outputDir, playerMapAvgOutputFile))
    playerMapGamemodeAvgs.to_csv(os.path.join(outputDir, playerMapGamemodeAvgOutputFile))

    print(os.path.join(outputDir, playerAvgOutputFile))
    print(os.path.join(outputDir, playerGamemodeAvgOutputFile))
    print(os.path.join(outputDir, playerMapAvgOutputFile))
    print(os.path.join(outputDir, playerMapGamemodeAvgOutputFile))

    success = 1

    return success

# debugging 
# processStats('logFiles/dataLog_06-11-2024.csv')