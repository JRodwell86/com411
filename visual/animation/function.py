#importing the visualisation stuff.
import matplotlib.pyplot as plt
# importing the animation stuff
import matplotlib.animation as animation

fig, ax = plt.subplots()

def animate(frame):
    #code to show the current frame
    print(f"Frame: {frame}")



def run():

    global fig
    #code for animation - calls the fig, the animate function, 10 frame and an interval of 1 second
    some_animation = animation.FuncAnimation(fig, animate, frames=10, interval=1000)

    #code to show the subplot
    plt.show()



run()