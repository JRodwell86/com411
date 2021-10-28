def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions

def menu():
    print("Please select a direction:")
    dirs = directions()
    for index in range(len(dirs)):
        movement =dirs[index]
        print(f"{index}: {movement}")

def run():
    menu()

if __name__ == "__main__":
    run()

