def observed():
    #empty list
    observations = []
    #while loop to select how many times to ask the question
    while len(observations) <= 6:

        observation = (input("Please enter an observation"))
        observations.append(observation)



def run():
    print("Counting observations...")
    #returning first function in a local variable
    seen = observed()
    #creating an empty set
    seen_set = set()
    for seen_set in seen:
        seen_set.count("Skyscraper")
    print(seen_set)

if __name__ == "__main__":
  run()