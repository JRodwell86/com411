# importing the visualisation stuff.
import matplotlib.pyplot as plt

import csv


# function to read data

def read_data():
    with open('temps.csv') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        temps = {'week1': [], 'week2': []}

        for values in csv_reader:
            temps['week1'].append(values[0])
            temps['week2'].append(values[1])

    print(temps)


def run():
    read_data()


if __name__ == "__main__":
    run()
