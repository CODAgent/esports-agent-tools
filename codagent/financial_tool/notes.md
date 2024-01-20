# Financial tool notes 

## Problems with just webscraping our site

- During the time between a tourney being done and a tourney being scraped, if we team on our site is deleted by a user, the tourney will show one less team because that team is now deleted
    - This affects the data base too 
    - The good thing is that the ID number on the end of our tourney links is the same as the challonge tourney id.
        - Turns out this is not the case 
        - I may need to search for challonge tourneys using the API
            - The ID field of a tourney in challonge is probably what corresponds to our tourney website
    - Solution 
        - Go thru challonge and get all of the tourney IDs we need 
        - Go thru the tourneys in challonge to get the number of teams that entered each tourney
        - Go thru our websites tourneys to get the other stats 
        - Dump this stuff into a CSV intelligently
            - Dont want duplicates
            - Dont want to ever delete data 

## Plan

- Need to get an accurate picture of tourney stats 
    - Main objectives 
        - Teams entered
        - Revenue in the tourney
        - Cost per team or person
        - Prize pool 
        - Our profit 

