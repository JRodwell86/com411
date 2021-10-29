#global variables
import csv
records = []
headings = []

def load_data(file_path):
    print("Loading data...", end="")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        print("Done!")

        for line in csv_reader:
            records.append(line)

def run():
    load_data("titanic.csv")
    print(f"Sucessfully loaded {len(records)} records")

if __name__ == "__main__":
  run()