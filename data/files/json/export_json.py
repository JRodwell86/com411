import json
#code to read contents of a json file
def read(file_path):
    print("Reading...")
    with open(file_path) as file:
        data = json.load(file)
    print("Done!")
#returns the data to a variable (called data in this case)
    return data
#file_path is where i want it to save. data is variable pulled from reading
def save(file_path, data):
    print("Exporting...")
    #code to export the file
    with open(file_path, "w") as file:
        json.dump(data, file, indent = 4)
        print("Done")

def run():
    #variable to create the data for save function. variable = call to read function
    json_data = read("robocity.json")
    #save, parameter 1 = file path, parameter 2 = variable of data pulled from reading.
    save("exported.json", json_data)


if __name__ == "__main__":
  run()