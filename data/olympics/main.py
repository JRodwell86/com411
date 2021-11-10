import csv
#importing the other code bits that have been made
import process
import tui

#file path has been entered in the call to function below.
def read_data(file_path):
#tui.started is the file structure to get to call function then can populate the file_path variable
    tui.started(f"Reading data from {file_path}")
#empty list
    data = []
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        #ignores the headings
        next(csv_reader)
        for line in csv_reader:
            data.append(line)
    tui.completed()
    return data


def run():
#calls the function read_data, populates with olympics info and puts it in to athelete data variable
    athlete_data = read_data("athlete_events.csv")
#while loop - as long as one of these is being chosen keep cycling through
    while True:
 #load the function in to a variable
        selection = tui.menu()
        if selection == "years":
#load the function something.something as is file path - athelete data is the variable created from the csv file
            process.list_years(athlete_data)
        elif selection == "tally":
            process.tally_medals(athlete_data)
        elif selection == "team":
            process.tally_team_medals(athlete_data)
        elif selection == "by years":
            process.record_by_year(athlete_data)
        elif selection == "exit":
#break ends the loop so it stops working through.
            break
        else:
#in brackets is the parameter msg in the error function
            tui.error("Invalid Selection!")


if __name__ == "__main__":
    run()