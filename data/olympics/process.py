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


def tally_medals(data):
    tui.started("Tallying medals")
    medal_tally = {"Gold": 0, "Silver": 0, "Bronze": 0}
    for record in data:
        medal = record[COL_MEDAL]
        if medal in ("Gold", "Silver", "Bronze"):
            medal_tally[medal] += 1
    tui.display_medal_tally(medal_tally)
    tui.completed()


def tally_team_medals(data):
    tui.started("Tallying medals for each team")
    medal_tally = {}
    for record in data:
        team = record[COL_TEAM]
        medal = record[COL_MEDAL]

        if medal not in ("Gold", "Silver", "Bronze"):
            continue

        if team in medal_tally:
            medal_tally[team][medal] += 1
        else:
            medal_tally[team] = {"Gold": 0, "Silver": 0, "Bronze": 0}
            medal_tally[team][medal] += 1

    tui.display_team_medal_tally(medal_tally)
    tui.completed()