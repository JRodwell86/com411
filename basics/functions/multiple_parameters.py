# define parameter of function
def climb_ladder(steps_remaining, steps_crossed):
    # if statement to calculate
    if steps_remaining > steps_crossed:
        print("Still some way to go!")
    else:
        print("We are almost there!")
# call to function

climb_ladder(5, 2)
climb_ladder(2, 5)
