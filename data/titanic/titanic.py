#global variables
import csv
records = []
headings = []

def load_data(file_path):
    print("Loading data...", end="")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        print("Done!")

        for line in csv_reader:
            records.append(line)

def display_menu():
    print(""" Please select one of the following options:
  [1] Display the names of all passengers
  [2] Display the number of passengers that survived
  [3] Display the number of passengers per gender
  [4] Display the number of passengers per age group""")
    response = int(input())
    return response

def display_passenger_names():
    print("The names of the passengers are:")
    for record in records:
        passenger_name = (record[3])
        print(passenger_name)


def run():
    load_data("titanic.csv")
    print(f"Sucessfully loaded {len(records)} records\n")
    selected_option = display_menu()
    print(f"You have selected option: {selected_option}")
    if selected_option == 1:
        display_passenger_names()
    else:
        print("Error! Option not recognised")

if __name__ == "__main__":
  run()