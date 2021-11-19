# importing the visualisation
import matplotlib.pyplot as plt
# importing the csv
import csv


# function to read data

def read_data():
    with open('temps.csv') as file:
        csv_reader = csv.reader(file)
        # removes headers from the text
        header = next(csv_reader)
        # makes a dictionary with the key pairs and second bit is list
        temps = {'week1': [], 'week2': []}
        # for loop to iterate through csv rows
        for values in csv_reader:
            # add the values from the first column to the list for first key value pairs. int to turn the string in
            # to numbers.
            temps['week1'].append(int(values[0]))
            # add the values from the first column to the list for second key value pairs. int to turn the string in
            # to numbers.
            temps['week2'].append(int(values[1]))

    return temps


def run():
    # call first function
    data = read_data()
    # create a variable for x axis - range number of records in CSV.
    # Could do len(data['week1']) and it returns for number of values in key value pairs
    x = range(1, 8)
    # 2 rows 1 column, sharex='col' means that the x axis will be shared in same column
    fig, axes = plt.subplots(2, 1, sharex='col')
    # axes[0] is the first one, data['week1/'] is all the values from key value pairs
    axes[0].plot(x, data['week1'])
    axes[1].bar(x, data['week2'])

    plt.show()


if __name__ == "__main__":
    run()
