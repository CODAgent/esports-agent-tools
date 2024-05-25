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

