# CODAgent Tourney Analytics Tool version 1.0

**NOTE: These instructions may change or be added to when there is a GUI Interface setup for Version 1.0**

## Prerequisites
1. Make sure you have cloned the repository and checked out a **new branch**
    - The instructions to do this can be found [here](../README.md)

2. Make sure you are on **your** branch.  To do this do the following within your terminal: 
    - Check what branch you are on:

        ``` 
        git branch 
        ```

        - Here you should see all of your branches.  The one you are on will be identified with a '*' next to the branch name
    - If you are not on your branch: 

        ``` 
        git checkout <your branch name> 
        ```

    - If you are not on your branch and have forgotten your branch's name:

        ``` 
        git checkout -b <give your branch a name> 
        git checkout <the branch name you just gave your branch>
        ```

3. Install the dependencies
    - Open your terminal
    - Make sure you are the "codagent" folder on your terminal
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

## How to mine data
1. Open up your terminal (CMD, PowerShell, Windows Terminal, Bash, etc.) 
2. cd to the "codagent" directory. Ex:

    ``` 
    cd /codagent 
    ```

3. Open the file called "main.py" and make sure the text in quotations on line 61 says 'mine'.
    
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

## How to filter data
- Coming soon

### How to filter data on already-filtered data
- Coming soon


--- 

### To Do List (for developer)
- [Click Here](TODO.md)

### Dependencies
- libraries
    - Selenium --> opens a web browser and runs tasks in it using a script.  need web browser drivers installed 
    - ChromeDriver downloads
    - BS4 --> built in python HTML parser.  scrapes using tags and attributes 
        - Scrapy is another option here
    - requests
    - re
- see requirements.txt



**NOTE:** I am using an environment for all of my dependencies called "codagent_tools"
