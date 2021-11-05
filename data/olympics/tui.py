#default value of the parameter is an empty string
def started(msg=""):
    print("-" * 85)
    print(f"Operation started: Reading data from {msg}...\n")

def completed():
    print("Operation completed")
    print("-" * 85)

def error(msg):
    print(f"Error! {msg}!")

def menu():
    print("""Please select one of the following options:
    [years] List unique years
    [tally] Tally up medals
    [ctally] Tally up medals for each team
    [exit] Exit the program""")
    print("Your selection:")
    msg = input()
    return msg

def display_medal_tally(tally):
    print(f"| Gold | {tally['Gold']}")

def run():

    started()
    completed()
    error("hi")
    menu()
    display_medal_tally({"Gold": 10, "Silver": 5, "Bronze": 2})

if __name__ == "__main__":
  run()