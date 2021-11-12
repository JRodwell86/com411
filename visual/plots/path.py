#importing the visualisation stuff.
#import matplotlib.pyplot as plt

def coordinate():
    x = int(input("Please enter a value for X"))
    y = int(input("Please enter a value for Y"))
    responses = (x, y)
    return responses

def path():
    print("Retrieving path...")
    coordinates = coordinate()
    x_values = []
    y_values = []

    for data in coordinates:



        x_values = coordinate()[1]
        y_values = coordinate()[2]


def run():

    responses = coordinate()

    print(responses)

if __name__ == "__main__":
    run()