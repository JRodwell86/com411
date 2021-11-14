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
    # don't need to create a variable as in the above as this is is the output of the function that is visualised with plt.show(). in '' is the colour, marker type & line type (green, square, dash
    plt.plot(x_values, y_values, 'gs--')


def large():
    y_values = [1, 6, 6, 1, 1]
    x_values = [1, 1, 6, 6, 1]
    # in '' is the colour, marker type & line type (blue, pentagon, solid line)
    plt.plot(x_values, y_values, 'bp-')




def run():
#calling each function
    small()
    medium()
    large()
#visualise the chart
    plt.show()

if __name__ == "__main__":
    run()