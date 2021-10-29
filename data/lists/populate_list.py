def directions():
    directions = ["Move Forward", "Move Backward","Turn Left","Turn Right"]
    return directions

def menu():
    print("Please select a direction:")
#The function should then call the first function and store the returned list in a local variable
    dirs = directions()
#The function should then use a loop to display each direction in the list with an index number.  This should be displayed in the format "{index}: {direction}" where {index} is the index number of the list and {direction} is the direction from the list.
    for index in range(len(dirs)):
        print(f"{index}: {dirs[index]}")
#The function should then read in the user's response.
    index = int(input())
#Finally, the function should return the direction corresponding to user's response.
    return dirs[index]

def run():
#The function should create an empty list named route
    route = []
    print("Working out escape route:")
#The function should then use a loop to do the following 5 times
    for count in range(5):
#Call the function menu and append the returned direction to the list route
        route.append(menu())
    print(f"Escape route: {route}")



if __name__ == "__main__":
    run()


