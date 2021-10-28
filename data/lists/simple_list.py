#function to create a list. Then return to

def directions():
#preopulated list
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
#returning the list to memory
    return directions


def run():
#printing the function so double brackets
    print(directions())


if __name__ == "__main__":
    run()
