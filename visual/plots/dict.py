# importing the visualisation stuff.
import matplotlib.pyplot as plt
# importing random number stuff
import random


def data():
    # empty dictionary
    paths = {}
    # variable for user input
    line_input = input("What kind of line would you like? (:, -- or -)")

    colour_input = input("What colour line would you like? Red(r), Green(g) or Blue(b)?")

    style_input = input("What style of marker would you like? Circle(o),Square(s) or Triangle(^)")

    # puts the key pairs in to the paths dictionary above - Key[""] = value
    paths["line"] = line_input
    paths["colour"] = colour_input
    paths["style"] = style_input
    # example of how to return just the value of the key pair
    print(f"{paths['colour']}")
    # return the inputs to the function
    return paths


def generate():
    # create variable for number if lines in graph
    lines = int(input("How many lines would you like to display?"))
    # how many times to go through the loop based on the input
    for values in range(lines):
        # create a list of dictionary info -
        # long winded see better method below.
        values = list(data().values())
        line = values[0]
        colour = values[1]
        style = values[2]

        # random number variable - 5 numbers between 1 and 25
        x = random.sample(range(1, 25), 5)
        y = random.sample(range(1, 25), 5)
        # create graph of this loop, x & y values and then line, colour, style
        plt.plot(x, y, f'{line}{colour}{style}')

    plt.show()


def run():
    print("Running...")
    generate()
    print("Done!")


if __name__ == "__main__":
    run()
# below is easier, instead of creating list above.
# variable to
# format = f"{values['colour']}{values['line_style']}{values['marker_style']}"
# plt.plot(x, y, format)
