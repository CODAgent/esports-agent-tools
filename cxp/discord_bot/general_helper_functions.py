def get_bot_token(inputFile):
    with open(inputFile, 'r') as fr:
        lines = fr.readlines()
    
    tokenStr = lines[0]
    return tokenStr

def execute_command(command, args_list):
    if command == list_of_commands[0]:      # delete_category_matches
        # for this command, we can only input one category
        category_given = ' '.join(args_list)
        print(command)
        print(category_given)


# takes in the path to the create matches csv
# returns a dictionary of the info from the csv 
#   away_team
#   away_team_discord_captain
#   home_team
#   home_team_discord_captain
def read_create_matches_csv(createMatchesCsvFile):
    with open(createMatchesCsvFile, 'r') as fr: 
        lines = fr.readlines()

    linesStripped = [x.strip('\n') for x in lines]

    header = linesStripped[0]
    body = linesStripped[1:len(linesStripped)]

    headerCols = header.split(',')

    createMatchesDict = {}
    for colIdx, colName in enumerate(headerCols):
        createMatchesDict[colName] = []

    createMatchesDictKeysList = list(createMatchesDict.keys())
    for rowIdx, row in enumerate(body):
        bodyCols = row.split(',')

        # away_team, away_team_discord, home_team, home_team_discord
        for bodyColIdx, bodyColVal in enumerate(bodyCols):
            createMatchesDict[createMatchesDictKeysList[bodyColIdx]].append(bodyColVal)

    return createMatchesDict

def create_match_names(createMatchesDict):
    match_names = []
    dictKeys = list(createMatchesDict.keys())

    for rowIdx, row in enumerate(createMatchesDict[dictKeys[0]]):
        away_team = createMatchesDict['away_team'][rowIdx]
        home_team = createMatchesDict['home_team'][rowIdx]

        match_name_preprocess = away_team + ' ' + home_team

        match_name = match_name_preprocess.replace(' ', '-').lower()

        match_names.append(match_name)
    return match_names 

        


# test = read_create_matches_csv('create_matches_input/test_input.csv')
# print(create_match_names(test))

