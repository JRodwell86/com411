#ask what kind of adventure
adventure = input("What type of adventure should I have?(scary/short/safe/long")
#identify the story
if (adventure == "scary") or (adventure == "short"):
    print("Entering the dark forest")
elif (adventure == "safe") or (adventure == "long"):
    print("Taking the safe route")
else:
    print("not sure which route to take")




