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
    - dipslay data based on filters 
        - idea: function input takes in a filter keyword, filter keyword triggers based on if statements
        - game
            - might need to scrape for the game because i don't think this is data that I currently scrape for 
        - monetary type of tourney 
        - team size type of tourney 
        - gamemode type of tourney 



## Main
- function that writes tourney info to a csv file

### Data grab
- make function that grabs all data --> **DONE**
    - loops through tourney ids and retrives the tourney infos in a list  
    
### GUI
- plotting graphs w/ different filters and parameters
- button for generating excel files 


---
## Housekeeping
- make "requirements.txt" file
- make git local repo --> **DONE**
- edit gitignore
- polish the readme 
- connect git local repo with a new esports agent repo --> **DONE**
