# How to use the CXP discord bot

1. Run ```python3 main.py``` in the terminal
2. In discord, type a command using the following format:
    ```
    cxp/<command> <arguments>
    ```

**NOTE:** The discord bot must be able to manage channels and messages in the server and the ```SERVER``` variable within ```main.py``` must **EXACTLY** match the server name.

## Supported commands 

- [Delete Category Channels](#-Delete-Category-Channels): ```delete_category_channels```
- [Create Category Match Channels](#-Create-Category-Matches): ```create_category_matches```

### Delete Category Channels

- How to run the command: 
    ```
    cxp/delete_category_matches <category_name>
    ```
- The terminal should log out which channels were deleted.  If any errors occur, the terminal will say what went wrong 
- NOTE: This only deletes text channels 
- NOTE: This does not delete the category you specify

### Create Category Matches 

- Need to setup an input CSV file at the following location: ```create_matches_input/input_file.csv```
    - The input file has the following columns: ```away_team```, ```away_team_discord_captain```, ```home_team```, ```home_team_discord_captain```
    - **NOTE:** The discord team captains must have their correct discord usernames in them
- Run the command:
    ```
    cxp/create_category_matches <category_name>
    ```

#### Notes 

- Might want to send a welcome message when the channels are created


