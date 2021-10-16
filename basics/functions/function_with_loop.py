## define parameter 0f function
def run():
    def cross_bridge(steps):
        # repeat crossed step for parameter
        for step in range(steps):
            print("Crossed Step")
    # if statement for too many steps
        if steps > 5:
            print("The bridge is collapsing!!")
        else:
            print("We must keep going!")

    # call to function
    cross_bridge(3)
    cross_bridge(6)