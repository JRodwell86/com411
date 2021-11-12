# importing the visualisation stuff.
import matplotlib.pyplot as plt


def coordinate():
    # inputs for values of x and y
    x = int(input("Please enter a value for X"))
    y = int(input("Please enter a value for Y"))
    # adds the input to the variable
    responses = (x, y)
    # returns the variable
    return responses


def path():
    print("Retrieving path...")
    # code to create empty lists
    x_values = []
    y_values = []
    # code below loops the rest 4 times.
    for data in range(4):
        # creates variable from the looped function above.
        coords = coordinate()
        # add the input from above in the lists
        x_values.append(coords[0])
        y_values.append(coords[1])
    # return the values in to the list
    return [x_values, y_values]


def run():
    # variable created from second function
    values = path()
    # enters the lists to plot the graph. Red, circle, dashed line.
    plt.plot(values[0], values[1], 'r^--')
    # visualises the graph
    plt.show()


if __name__ == "__main__":
    run()
