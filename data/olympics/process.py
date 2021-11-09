import tui
#variables to show the position in the dictionary
COL_MEDAL = 14
COL_TEAM = 6
COL_YEAR = 9

#data is athelete_events and added in the main
def list_years(data):
#function and parameter for the start of the file - puts in the thing
    tui.started("Listing years")
#empty set
    years = set()
#for new variable in the athelete events csv
    for record in data:
#variable is the data[column in data]
        year = record[COL_YEAR]
#adding the year info the the empty year set.
        years.add(year)
#adds the set as a parameter in the display_years function so when it is called it populates
    tui.display_years(years)
#calls a function to print off an end portion of the display
    tui.completed()

#data is athelete_events and added in the main
def tally_medals(data):
#calling the function and entering the parameter if this one is chose
    tui.started("Tallying medals")
#creating a list of 0 for each tally so it can then be counted up
    medal_tally = {"Gold": 0, "Silver": 0, "Bronze": 0}
#for new variable in athelete_events
    for record in data:
##variable is the data[column in data]
        medal = record[COL_MEDAL]
#if the medal (identified line by line in data above) is one of the below
        if medal in ("Gold", "Silver", "Bronze"):
#then add 1 to the tally of the specific area
            medal_tally[medal] += 1
#adds the list as a parameter to the function
    tui.display_medal_tally(medal_tally)
#calls a function to print off an end portion of the display
    tui.completed()

#data is athelete_events and added in the main
def tally_team_medals(data):
    # calling the function and entering the parameter if this one is chose
    tui.started("Tallying medals for each team")
#empty list for medal tally
    medal_tally = {}
#for a new variable in athelete events
    for record in data:
##variable is the data[column in data]
        team = record[COL_TEAM]
        medal = record[COL_MEDAL]
#if the medal (identified line by line in data above) is not inone of the below
        if medal not in ("Gold", "Silver", "Bronze"):
#if there is no info for gold, silver, bronze in the medal variable then skip over the rest and start loop again
            continue
#if team (from the data column) is in blank variable medal tally. To be in the blank list it would be created in the else below. So first time there would be nothing and it would be added. second time it would just add to exisiting.
        if team in medal_tally:
# if medal is gold, silver, bronze then a new list is created of team name + medal. first and second variable are the key pairs.
            medal_tally[team][medal] += 1
        else:
#this statement creates the list for the above if statement to then fill in.
            medal_tally[team] = {"Gold": 0, "Silver": 0, "Bronze": 0}
            medal_tally[team][medal] += 1
    # adds the list as a parameter to the function
    tui.display_team_medal_tally(medal_tally)
    # calls a function to print off an end portion of the display
    tui.completed()