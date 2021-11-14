# importing the visualisation stuff.
import matplotlib.pyplot as plt
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

    # print(paths)
    return paths


def generate():
    x_values = []
    y_values = []

    lines = int(input("How many lines would you like to display?"))
    for values in range(lines):
        values = data()
        for value in values.values():
            choice = [value]
            print(choice)

        randomlistx = random.sample(range(1, 25), lines)
        randomlisty = random.sample(range(1, 25), lines)
        x_values.append(randomlistx)
        y_values.append(randomlisty)
        plt.plot(x_values, y_values, 'r^--')
        plt.show()

def run():
    print("Running...")
    generate()
    print("Done!")


if __name__ == "__main__":
    run()
