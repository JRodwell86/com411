def steps():
  likelihoods = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
  return likelihoods

def run():
#call the first function and store the returned list in a local variable
  value = steps()
#create two empty lists
  good_steps = []
  bad_steps = []
#for loop to find tuple items [1] that are more that 50
  for step in value:
    if (step[1] >= 50):
#code to append those items to the blank lists above
      bad_steps.append(step)
    else:
      good_steps.append(step)
#len to count the number of steps
  print(f"Good steps: {len(good_steps)}, Bad Steps: {len(bad_steps)}")




if __name__ == "__main__":
    run()
