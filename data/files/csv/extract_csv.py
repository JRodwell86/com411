import csv

def extract (file_path):
    #the end="" means that there is no new line between extracting... and done! they are joined together.
    print("Extracting...",end="")

    with open(file_path) as file:
        csv_reader = csv.reader(file)

        next(csv_reader)
        #blank string variable that you can put things in
        names = ""

        for data in csv_reader:
            #returning information to the names variable from the specific row/column of information
            names += f"{data[1]}\n"
            #below printing is not indented as needs to be outside the loop otherwise results repeat.
        print("Done!")
        print(f"The extracted names are as follows:\n{names}")



def run():
    extract("bots.csv")


if __name__ == "__main__":
  run()