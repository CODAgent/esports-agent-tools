# TODO

## Web Scraper
- web scraper function for one tourney --> **DONE**
- make 'tournament_id_getter' function that checks each link to see if it is a valid tournament and adds it to a list of ids --> **DONE**
- make 'tournament_id_getter' function better --> **DONE**
    - scrape from the esportsagent.gg/tournament site, get the ahrefs and get the links to the tourneys we want
- fix platforms bug --> **DONE** 
    - issue when there is not a platform included

## CSV writer
- goal is just to display the data wanted in an easy format
- options
    - display all data no matter what kind of tourney it is --> **DONE**
    - basically need a function that fetches data on the site and dumps it into a large csv file --> **DONE** *has NOT been stress tested yet*
        - this large csv file will contain all the data from when this tool is deployed
        - the function needs to check if there is already an 'all data' csv file
            - if yes --> then collect all the data from that file and append the new, unique data from the site to it
            - if no --> easy case: create the csv file with the site data 
    - dipslay data based on filters --> this will be done from the 'all data' csv file, no web scrapping is needed for this because it should have already been done before
        - idea: function input takes in a filter keyword, filter keyword triggers based on if statements
            - want to display the data exactly the same as the 'all data' file, just for simplicity, readability, and to make it easier on the developer (me) 
        - game
            - might need to scrape for the game because i don't think this is data that I currently scrape for 
                - it seems that the only place where the game is mentioned is in the tourney title --> will try to solve this issue later
        - date --> **DONE**
        - monetary type of tourney 
            - Free Entry 
            - Paid Entry
            - Free Entry No Prize
        - team size type of tourney 
            - 1v1
            - 2v2
            - 3v3
            - 4v4
        - gamemode type of tourney --> this is also only found in the title, will handle this issue later
            - variant
            - snd
            - other
        - series type
            - best of 1 
            - best of 3 
            - best of 5
        - tourney type (single, double elim)
            - single elim
            - double elim
        - number of teams registered 
            - input a threshold amount (greater than, less than, equal to)
        - prize pool 
            - input a threshold amount
        - buy in 
            - input a threshold amount 
- add infrastructure for a backup all data file --> **DONE**
    - maybe look into an automated script to do this? 
    - maybe even look into an automated data mining script (one that does so every other day or something)



## Main
- function that writes tourney info to a csv file

### Data grab
- make function that grabs all data --> **DONE**
    - loops through tourney ids and retrives the tourney infos in a list  
    
### GUI
- plotting graphs w/ different filters and parameters
- button for generating filtered csv files 
- button to mine data? 

## Mining 
- need to add infrastructure to mine data every 1 or 2 days 
- based on where the 'all data' file will be stored, I may need to change some path stuff for the csv writing 


---
## Housekeeping
- make "requirements.txt" file
- make git local repo --> **DONE**
- edit gitignore
- polish the readme 
- connect git local repo with a new esports agent repo --> **DONE**

--- 
## For Version 2.0
- automate 
- sort all data by date to make filtering quicker 
