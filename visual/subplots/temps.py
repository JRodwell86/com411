# importing the visualisation stuff.
import matplotlib.pyplot as plt


# function to read data

def read_data(file_path):
    # empty list
    temps = []
    # opening the file in read mode
    with open(file_path) as file:
        # loop to iterate through txt lines
        for line in file:
            # adding to list as numbers and strip to remove gaps and \n
            temps.append(int(line.strip()))
        # return the list to the function
        return temps


def run():
    # call first function and assign data to variable
    data = read_data('temps.txt')
    # create a figure of 2 axes
    fig, (axes) = plt.subplots(1, 2)
    # assign x & y variables
    x = range(len(data))
    y = data
    # create different axes from data
    axes[0].plot(x, y)
    axes[1].bar(x, y)
    # display the graphs
    plt.show()


if __name__ == "__main__":
    run()
