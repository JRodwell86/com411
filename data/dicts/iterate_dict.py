def pattern():
#blank dictionary
    sequences = {}
#adding contents of dictionary
    sequences = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence": 1}
#returning the dict to the function
    return sequences


def display_keys(data):
#key is an identifier - will always return the 'key' - data is the returned dictionary.
    for key in data:

        print(key)

def run():
    #create variable from the first function
    data = pattern()
    #put that variable (dictionary) in to the second function
    display_keys(data)

if __name__ == "__main__":
  run()