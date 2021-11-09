#defining how wide we want the line to be.Means that it can be easily changed without having to change the function.
LINE_WIDTH = 85

#this is the start comment that it is put in and populated in the process section by the parameter there.
def started(msg=""):
#creates a variable that put in the variable with phrase.
    output = f"Operation started: {msg}..."
#creates variable for dashes line
    dashes = "-" * LINE_WIDTH
#prints the two created variables above.
    print(f"{dashes}\n{output}\n")


def completed():
#makes the line without having the change the function if need to change the width.
    dashes = "-" * LINE_WIDTH
#prints
    print(f"\nOperation completed.\n{dashes}\n")

#prints an error message populated by the thing created in process.
def error(msg):
    print(f"Error! {msg}\n")


def menu():
    print(f"""Please select one of the following options:
    {"[years]":<10} List unique years
    {"[tally]":<10} Tally up medals
    {"[team]":<10} Tally up medals for each team
    {"[exit]":<10} Exit the program
    """)
    selection = input("Your selection: ")
#strips out any spaces and also makes it lower case and returns input to function to be called in process.
    return selection.strip().lower()

#loads list from the process section and identifies what part of tally to use from the key pair.
def display_medal_tally(tally):
    print(f"| {'Gold':<10} | {tally['Gold']:<10} |")
    print(f"| {'Silver':<10} | {tally['Silver']:<10} |")
    print(f"| {'Bronze':<10} | {tally['Bronze']:<10} |")


def display_team_medal_tally(team_tally):
#For the key pair items in the list made by items() method is used to return the list with all dictionary keys with values.
    for team, tally in team_tally.items():
        print(team)
        print(f"\tGold:{tally['Gold']}, Silver:{tally['Silver']}, Bronze:{tally['Bronze']}")


def display_years(years):
#the sorted bit orders the output in to reverse order. (normal order - sorted(years)
    sorted_years = sorted(years, reverse=True)
    for year in sorted_years:
        print(year)