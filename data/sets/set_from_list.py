def observed():
    #empty list
    observations = []
    #while loop to select how many times to ask the question
    while len(observations) <= 6:
#code to add answers to question straight to the list
        print("Please enter an observation")
        observations.append(input())
#returning the answers to the list and therefore the function
    return observations


def run():
    print("Counting observations...")
    #returning first function in a local variable
    observations = observed()
    #creating an empty set
    observations_set = set()
    #observation is a new variable for this for loop
    for observation in observations:
    #create a variable to store the info in. So reads the variable and second part counts how many times variable appears
        data = (observation, observations.count(observation))
    #add the data that i've found to the blank set
        observations_set.add(data)
    #data variable stored in the observations_set
    for data in observations_set:
    #print the positions of the data in the set. 0 = observation name and 1 = times mentioned
        print(f"{data[0]} observed {data[1]} times.")

if __name__ == "__main__":
  run()