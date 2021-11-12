# importing the visualisation stuff.
import matplotlib.pyplot as plt


def data():
    paths = {}

    line_input = input("What kind of line would you like? (:, -- or -)")

    colour_input = input("What colour line would you like? Red(r), Green(g) or Blue(b)?")

    style_input = input("What style of marker would you like? Circle(o),Square(s) or Triangle(^)")

    paths = {"line": line_input, "colour": colour_input, "style": style_input}

    print(paths)

def run():
    data()

if __name__ == "__main__":
  run()