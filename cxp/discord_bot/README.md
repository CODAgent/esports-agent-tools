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
    cxp/delete_category_channels <category_name>
    ```
- The terminal should log out which channels were deleted.  If any errors occur, the terminal will say what went wrong 
- NOTE: This only deletes text channels 
- NOTE: This does not delete the category you specify

### Create Category Matches 

#### Notes 

- Want the CSV to contain the following columns 
    - away team 
    - home team 
    - away team captain discord username 
    - home team captain discord username 



