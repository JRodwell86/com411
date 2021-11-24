#importing the visualisation stuff.
import matplotlib.pyplot as plt
# importing the animation stuff
import matplotlib.animation as animation

def animate(frame):
    # code to show the current frame
    print(f"Frame: {frame}")

# your code here

def run():
        # your code here (use fig with animation function)
    fig, ax = plt.subplots()
    #code for animation - calls the fig, the animate function, 10 frame and an interval of 1 second
    some_animation = animation.FuncAnimation(fig, animate, frames=10, interval=1000)
    #code to show the subplot
    plt.show()


run()