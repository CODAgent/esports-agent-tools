# How to use the CXP discord bot

1. Run ```python3 main.py``` in the terminal
2. In discord, type a command using the following format:
    ```
    cxp/<command> <arguments>
    ```

**NOTE:** The discord bot must be able to manage channels in the server and the ```SERVER``` variable within ```main.py``` must **EXACTLY** match the server name.

## Supported commands 

- [Delete Category Channels](### Delete Category Channels): ```delete_category_channels```

### Delete Category Channels

- How to run the command: 
    ```
    cxp/delete_category_channels <category_name>
    ```
- The terminal should log out which channels were deleted.  If any errors occur, the terminal will say what went wrong 
- NOTE: This only deletes text channels 
- NOTE: This does not delete the category you specify
