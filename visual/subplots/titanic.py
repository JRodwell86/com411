# importing the visualisation
import matplotlib.pyplot as plt
# importing the csv
import csv

def read_data():
    with open('titanic.csv') as file:
        csv_reader = csv.reader(file)
        # removes headers from the text
        header = next(csv_reader)