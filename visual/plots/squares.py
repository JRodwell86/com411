#importing the visualisation stuff.
import matplotlib.pyplot as plt

#making a small square
def small():
    y_values = [3, 4, 4, 3, 3]
    x_values = [3, 3, 4, 4, 3]
#making variable that contains square info. in '' is the colour, marker type & line type (red, circle, dot)
    small = plt.plot(x_values, y_values, 'ro:')
#return variable to the function
    return small

def medium():
    y_values = [2, 5, 5, 2, 2]
    x_values = [2, 2, 5, 5, 2]
    # making variable that contains square info. in '' is the colour, marker type & line type (green, square, dash
    med = plt.plot(x_values, y_values, 'gs--')
    # return variable to the function
    return med

def large():
    y_values = [1, 6, 6, 1, 1]
    x_values = [1, 1, 6, 6, 1]
    # making variable that contains square info. in '' is the colour, marker type & line type (blue, pentagon, solid line)
    large = plt.plot(x_values, y_values, 'bp-')
    # return variable to the function
    return large



def run():
#calling each function
    small()
    medium()
    large()
#visualise the chart
    plt.show()

if __name__ == "__main__":
    run()