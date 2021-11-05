def pattern():
#blank dictionary
    sequences = {}
#adding contents of dictionary
    sequences = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence": 1}
#returning the dict to the function
    return sequences

def run():
#code to print the dict from the function
    print(pattern())

if __name__ == "__main__":
  run()