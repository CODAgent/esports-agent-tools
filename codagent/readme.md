# <a id="codagenttool">CODAgent Tourney Analytics Tool Version 1.0</a>

**NOTE: These instructions may change or be added to when there is a GUI Interface setup for Version 1.0**

---

## <a id="codagenttoolprereqs">Prerequisites</a>

1. If you haven't already, follow the setup steps [here](../README.md#setup).
2. Make sure you have cloned the repository and checked out a **new branch**
    - The instructions to do this can be found [here](../README.md#clonerepo)

3. Make sure you are on **your** branch.  To do this do the following within your terminal: 
    - Check what branch you are on:

        ``` 
        git branch 
        ```

        - Here you should see all of your branches.  The one you are on will be identified with a '*' next to the branch name
    - If you are not on your branch: 

        ``` 
        git checkout your-branch-name 
        ```

    - If you are not on your branch and have forgotten your branch's name, make a new one by following [these steps](../README.md#createbranch).

4. Install the dependencies
    - Open your terminal
    - Make sure you are in the "codagent" folder on your terminal
        - If you are not then use cd: 

            ``` 
            cd /codagent 
            ```

    - Type the following into your terminal: 

        ```
        pip3 install -r requirements.txt
        ```

        OR

        ```
        pip install -r requirements.txt
        ```

---

## <a id="codagenttoolminedata">How to mine data</a>

1. Open up your terminal (CMD, PowerShell, Windows Terminal, Bash, etc.) 
2. cd to the "codagent" directory. Ex:

    ``` 
    cd /codagent 
    ```

3. Open the file called "main.py" and make sure the text in the following line of code says 'mine' (line 56):

    ```action = define_action('mine')```
    
    - If this text does say 'mine', then proceed to step 4. 
    - If this text does not say 'mine', then change this text to say 'mine' and proceed to step 4.

4. Run "main.py" by typing this into your terminal and pressing Enter

    ``` 
    python3 main.py 
    ```

    - You might need to type this: 

        ``` 
        python main.py 
        ```

    - At this point the program should run for a few minutes and print a statement in the terminal.  The following is what each statement means:
        - "Done.  New file created."
            - This means that a mining file has not been created before and is being created for the first time.  You should now see this CSV file in your File Explorer.
        - "Done.  New data written."
            - This means that your mining should have been successful and you should see new data if you open up the CSV file in your File Explorer.
        - "Done.  No new data written."
            - This means that the data in your CSV file already contains the most up-to-date data.

5. Once you are positive that you have properly mined new data, in your terminal type the following:

    ```
    git add all_data.csv
    git commit -m "new data mined"
    git push
    ```

6. After step 5, navigate to the following link: [Esports Agent Tools Repository](https://github.com/CODAgent/esports-agent-tools/)

7. Go to the "Pull Requests" tab and click the button that says "New Pull Request".

8. From here, you should see a drop down that points to another drop down, right below the section that says "Compare changes".  You want the drop downs to show as: base:master <-- compare: "your branch name".  These usually do not originally say this, so just click on the right-hand drop down menu and select your branch.
    - If this is what the drop downs say, then click the "Create pull request" button.  After this you are done!
    - If you are unable to get the drop downs to appear properly or if there is another error, contact the developer: [LonelyDock3](https://twitter.com/lonelydock3)

## <a id="codagenttoolfilterdata">How to filter data</a>

**NOTE: You should NOT push any filtered data to the repository and, in fact, the way the repository is setup, you are not able to do so.**

This means that once you filter data and look at the data, it is strongly recommended that you delete the filtered file.

1. Open up your terminal (CMD, PowerShell, Windows Terminal, Bash, etc.) 
2. cd to the "codagent" directory. Ex:

    ``` 
    cd /codagent 
    ```

3. Open the file called "main.py" and make sure the text in the following line of code says 'filter' (line 56):
    
    ```action = define_action('filter')```

    - If this text does say 'filter', then proceed to step 4. 
    - If this text does not say 'filter', then change this text to say 'filter' and proceed to step 4.

4. There is a very specific way to filter specific data and this is done by editing certain fields in the "main.py" file in the "filter\_write" function located on line 77.

    The "filter\_write" function is formated as follows: 
    
    ``` filter_write(filter_category, [filter_criterion]) ```
    
    It is recommended that you do not touch the "path" or "output\_path" inputs for filtering.
    
    The following exact terms are valid for the "filter\_category" input:
    - 'date'
        - Filters by date
    - 'money'
        - Filters by buy-in price
    - 'platforms' 
        - Filters by platforms (Console only, PC)
        - *NOTE: There is a bug in the data mining for platforms so it is useless to use the platform filter right now*
    - 'team size'
        - Filters by team size
    - 'elimination type'
        - Filters by single or double elimination
    - 'number of teams'
        - Filters by number of teams that entered the tourney 
    - 'series type'
        - Filters by the series type (Best of 1, 3, 5)
    - 'prize'
        - Filters by the prize pool amount 
    
    The following are the accepted "filter\_criterion" input formats for each "filter\_category" for filtering:
    - 'date'
        - Input two days, ex: ['September 22, 2022', 'September 23, 2022']
        - Input a month, ex: ['September 2022']
        - Input a year, ex: ['2022']
    - 'money'
        - Input for free entry: ['free entry']
        - Input for paid entry: ['paid entry']
        - Input for free entry no prize: ['free entry no prize']
        - Input a threshold amount (can only do greater than or less than)
            - ex: ['>,4.9']
            - ex: ['<,4.9']
    - 'platforms' 
        - Input for console only: ['console only']
        - Input for pc only: ['pc only']
        - Input for cross-platform: ['all']
    - 'team size'
        - Input for 1v1: ['1v1']
        - Input for 2v2: ['2v2']
        - Input for 3v3: ['3v3']
        - Input for 4v4: ['4v4']
        - Input for 5v5: ['5v5']
        - Input for 6v6: ['6v6']
    - 'elimination type'
        - Input for single elimination: ['single']
        - Input for double elimination: ['double']
    - 'number of teams'
        - Input a threshold amount (can only do greater than or less than)
            - ex: ['>,4.9']
            - ex: ['<,4.9']
    - 'series type'
        - Input for bo1: ['Best of 1']
        - Input for bo3: ['Best of 3']
        - Input for bo5: ['Best of 5']
    - 'prize'
        - Input a threshold amount (can only do greater than or less than)
            - ex: ['>,4.9']
            - ex: ['<,4.9']
    
    
    *NOTE: You can also get a brief guide to using these if you edit line 56 in "main.py" to say 'how to filter' and then you run main.py in your terminal.*
    
    **TO FILTER:** Change the text within the "filter\_category" and the "filter\_criterion" within the "filter\_write" function on line 77 to the desired criteria you would like to filter out of all the data, based on the valid inputs above.

5. Run "main.py" by typing this into your terminal and pressing Enter

    ``` 
    python3 main.py 
    ```

    - You might need to type this: 

        ``` 
        python main.py 
        ```
From here a file should have been generated called "filtered_data.csv".  You can open this file to see the filtered data.

### <a id="codagenttoolfilteronfilterdata">How to filter data on already-filtered data</a>

1. To filter data that has already been filtered or, in other words, is within the "filtered\_data.csv" file, follow steps 1-4 [here](#codagenttoolfilterdata).

2. After step 3 in the filter data guide, you must change the inputs called "path" and "output\_path", within the "filter_write" function in the "main.py" file on line 77, as follows:
    - For the "path" input, change this to say 'filtered\_data.csv'.
    - For the "output\_path" input, change this whatever you would like, but make sure it begins with 'filtered_' and it ends with '.csv'
        - Ex: 'filtered\_on\_filtered\_data.csv'

    Here's an example of how "filter\_write" should look: ``` filter_write('date', ['September 22, 2022', 'September 22, 2022'], path='filtered_data.csv', output_path='filtered_on_filtered_data.csv') ```

3. Do step 5 from [here](#codagenttoolfilterdata) and then you will have your new super filtered data located at the file called whatever you named the "output\_path" input in the "filter\_write" function of the "main.py" file.

--- 

### <a id="codagenttooltodo">To Do List (for developer)</a>

- [Click Here](TODO.md)

### <a id="codagenttooldependencies">Dependencies</a>

- libraries
    - Selenium --> opens a web browser and runs tasks in it using a script.  need web browser drivers installed 
    - ChromeDriver downloads
    - BS4 --> built in python HTML parser.  scrapes using tags and attributes 
        - Scrapy is another option here
    - requests
    - re
- see requirements.txt



**NOTE:** I am using an environment for all of my dependencies called "codagent_tools"
