#importing the visualisation stuff.
import matplotlib.pyplot as plt


def display(x_values, y_values):

#displaying the graph based on the parameters in the run function.
    plt.plot(x_values, y_values)
    plt.show()

def run():
# lists of x and y values
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 4, 9, 16, 25]
# code for labelling the axis
    plt.xlabel("x values")
    plt.ylabel("y values")
# call to display function with parameters
    display(x_values, y_values)


if __name__ == "__main__":
    run()