#import csv not needed as not reading the file, just writing

def export (file_path, integer):

    print("Exporting...")
#using a as 'appending' to an existing file
    with open(file_path, "a") as file:
        #don't need the below in this as not reading, just writing
        #csv_reader = csv.reader(file)
        #next(csv_reader)

        #range is counting the number of times I want to add new info.
        for count in range(integer):
            print("Please enter the bot ID:")
            bot_id = int(input())
            print("Please enter the bot name:")
            bot_name = input()
            print("Please enter the bot paint")
            bot_paint = input()
#creating a variable for the data i want to add. then writing the variable.
            data = f"{bot_id},{bot_name},{bot_paint}\n"
            file.write(data)

    print("Done!")
#code to call to function, with file_path and integer for number of data to enter.
def run():
    export("exported_bots.csv", 2)

if __name__ == "__main__":
  run()