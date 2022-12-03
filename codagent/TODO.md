# TODO

## Web Scraper
- web scraper function for one tourney --> **DONE**
- make 'tournament\_id\_getter' function that checks each link to see if it is a valid tournament and adds it to a list of ids --> **DONE**
- make 'tournament\_id\_getter' function better --> **DONE**
    - scrape from the esportsagent.gg/tournament site, get the ahrefs and get the links to the tourneys we want
- fix platforms bug --> **DONE** 
    - issue when there is not a platform included
- platform bug 
    - when there is a console only tournament, the data is scrapped as an all platform tournament
    - this will probably be broken until a certain date, until then all scraped data for platform stuff is inaccurate

## CSV writer
- goal is just to display the data wanted in an easy format
- options
    - display all data no matter what kind of tourney it is --> **DONE**
    - basically need a function that fetches data on the site and dumps it into a large csv file --> **DONE** *has NOT been stress tested yet*
        - this large csv file will contain all the data from when this tool is deployed
        - the function needs to check if there is already an 'all data' csv file
            - if yes --> then collect all the data from that file and append the new, unique data from the site to it
            - if no --> easy case: create the csv file with the site data 
    - dipslay data based on filters --> this will be done from the 'all data' csv file, no web scrapping is needed for this because it should have already been done before --> **DONE**
        - idea: function input takes in a filter keyword, filter keyword triggers based on if statements
            - want to display the data exactly the same as the 'all data' file, just for simplicity, readability, and to make it easier on the developer (me) 
        - game --> for version 2.0
            - might need to scrape for the game because i don't think this is data that I currently scrape for 
                - it seems that the only place where the game is mentioned is in the tourney title --> will try to solve this issue later
        - date --> **DONE**
        - monetary type of tourney --> **DONE**
            - Free Entry 
            - Paid Entry
            - Free Entry No Prize
        - platform --> **DONE**
            - Console only
            - PC only 
            - All
        - team size type of tourney --> **DONE**
            - 1v1
            - 2v2
            - 3v3
            - 4v4
        - gamemode type of tourney --> this is also only found in the title, will handle this issue later --> add this for version 2.0
            - variant
            - snd
            - other
        - series type --> **DONE**
            - best of 1 
            - best of 3 
            - best of 5
        - tourney type (single, double elim) --> **DONE**
            - single elim
            - double elim
        - number of teams registered --> **DONE**
            - input a threshold amount (greater than, less than, equal to)
        - prize pool --> **DONE**
            - input a threshold amount
        - buy in --> **DONE**
            - free entry
                - issue here because switcheroos are denoted as $0 buy-ins
            - paid entry 
            - free entry no prize
            - input a threshold amount 
- add infrastructure for a backup all data file --> **DONE**
    - maybe look into an automated script to do this? 
    - maybe even look into an automated data mining script (one that does so every other day or something)
- make documentation document for the filtering --> **DONE**



## Main
- function that writes tourney info to a csv file --> **DONE**

### Data grab
- make function that grabs all data --> **DONE**
    - loops through tourney ids and retrives the tourney infos in a list  
    
### GUI
- button to mine data --> **DONE**
- button for generating filtered csv files --> **DONE**
    - specify input file 
    - specify output file
- plotting graphs w/ different filters and parameters --> **DONE**
- get averages of data with filters on 
- currently creating GUI skeleton in codagent\_tool.py but will be editing main.py to house the GUI code --> **DONE, except for the help buttons**
- layout (button on top, three 'frames' below it)
    - top button --> mining button
    - left side --> options
        - checkboxes of different options for an action button --> **DONE**
        - at the very bottom you need to select your input file (all_data.csv, filtered_data.csv, etc) --> **DONE**
        - add functionality
    - right side --> actions 
        - filter
            - can do this for unlimited number of checked options 
                - might need to have the user specify which order to filter if theres multiple options? 
            - need to specify your output file name here, will be a CSV file no matter what
        - plot
            - 2D plots for now
            - check two options
            - under plot you declare which of the checked boxes will be your x axis and which will be your y axis
        - get stats
            - for a max of 2 options
            - returns all options' means, modes, standard deviations, and variances
            - returns covariance matrix that compares option 1 and option 2
    - very right side --> help
        - help button for each action button that describes in a message box, how to use the button with the options

## Mining 
- need to add infrastructure to mine data every 1 or 2 days 
- based on where the 'all data' file will be stored, I may need to change some path stuff for the csv writing 


---
## Housekeeping
- make "requirements.txt" file --> *Needs to be updated* 
    - pip3  install bs4
    - pip3  install selenium
    - pip3  install webdriver-manager
    - pip3 install requests
    - pip3 install tk OR apt-get install python3-tk
    - to run a requirements file: pip3 install -r requirements.txt
    - to make requirements file: pip freeze > requirement.txt
- make git local repo --> **DONE**
- edit gitignore
- polish the readme 
    - main readme --> **DONE**
        - how to clone repo --> **DONE**
        - how to create a branch --> **DONE** 
        - how to update your branch to the latest changes --> **DONE**
        - codagent readme --> **DONE** 
            - how to mine --> **DONE**
            - how to filter --> **DONE**
                - how to filter filtered --> **DONE**
- connect git local repo with a new esports agent repo --> **DONE**

--- 
## For Version 2.0
- automate 
- sort all data by date to make filtering quicker --> **DONE**
- fix issue on filtering where switcheroos appear as a $0 buy-in
- add filtering for gamemode
- add filtering for different games
- add support for plotting multiple lines on a plot
