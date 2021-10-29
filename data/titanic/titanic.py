#global variables
import csv
records = []
headings = []

def load_data(file_path):
    #adding global and variable name means that the variable i do below 'headings' goes to the global one
    global headings
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
  [4] Display the number of passengers per age group
  [5] Display the number of survivors per age group""")
    response = int(input())
    return response

def display_passenger_names():
    print("The names of the passengers are:")
    for record in records:
        passenger_name = (record[3])
        print(passenger_name)

def display_num_survivors():
#variable to make the count for the num_survived
    num_survived = 0
#for loop to go through all the records.
    for record in records:
# int to make it a number. square brackets to show the position.
        survival_status = int(record[1])
        if survival_status == 1:
# adds the number to the variable that I have put
            num_survived += 1
    print(f"{num_survived} passengers survived.")

def display_passengers_per_gender():
    females = 0
    males = 0

    for record in records:
        gender = (record[4])
# the .lower means that it reads the variable as lower case whether it is or not.
        if gender.lower() == "male":
            males += 1
        else:
            females += 1
    print(f"Females: {females} Males: {males}")

def display_passengers_per_age_group():
    children = 0
    adults = 0
    elderly = 0

    for record in records:
#code to ignore any blank strings in the lists
        if record[5] != "":
#float converts number in a string to an integer cos is from list
            age = float(record[5])
            if age < 18:
                children += 1
            elif age >= 65:
                 elderly += 1
            else:
                adults += 1
    print(f"Children:{children}, Adults:{adults}, Elderly:{elderly}")


def display_survivors_per_age_group():

    for record in records:

        if int(record[1]) == 1:
            survivors = record

            children = 0
            adults = 0
            elderly = 0

            for survivor in survivors:
                if survivor[5] != "":
                    age = float(survivor[5])
                    if age < 18:
                        children += 1
                    elif age >= 65:
                        elderly += 1
                    else:
                        adults += 1
            print(children)

def run():
    load_data("titanic.csv")
    print(f"Sucessfully loaded {len(records)} records\n")
    selected_option = display_menu()
    print(f"You have selected option: {selected_option}")
    if selected_option == 1:
        display_passenger_names()
    elif selected_option == 2:
        display_num_survivors()
    elif selected_option == 3:
        display_passengers_per_gender()
    elif selected_option == 4:
        display_passengers_per_age_group()
    elif selected_option == 5:
        display_survivors_per_age_group()
    else:
        print("Error! Option not recognised")


if __name__ == "__main__":
  run()