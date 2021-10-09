#steps to count
steps = int(input("How far are we from the cave?"))
print("")
#countdown
for count in range(steps,0,-1):
    print(f"{steps} steps remaining")
    steps = steps - 1
print("")
print("We have reached the cave!")