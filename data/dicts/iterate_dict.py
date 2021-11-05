def pattern():
#blank dictionary
    sequences = {}
#adding contents of dictionary
    sequences = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence": 1}
#returning the dict to the function
    return sequences


def display_keys(data):
    print("Keys:")
#key is an identifier - will always return the 'key' - data is the returned dictionary.
    for key in data:
        print(key)

def display_values(data):
    print("\nValues:")
    for value in data.values():
        print(value)

def display_items(data):
    print("\nPairs:")
    for key, value in data.items():
        print(f"{key}, {value}")

def run():
    #create variable from the first function
    data = pattern()
    #put that variable (dictionary) in to the second function
    display_keys(data)
    display_values(data)
    display_items(data)

if __name__ == "__main__":
  run()