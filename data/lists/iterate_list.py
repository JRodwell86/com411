def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

def menu():
    print("Please select a direction:")
    dirs = directions()
#code to identify index points of a list
    for index in range(len(dirs)):
        #code to show index number and the list items from that index position.
        print(f"{index}: {dirs[index]}")

def run():
    menu()

if __name__ == "__main__":
    run()

