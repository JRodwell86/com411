#importing the visualisation stuff.
import matplotlib.pyplot as plt
# importing the animation stuff
import matplotlib.animation as animation
# import math stuff
import math

fig, ax = plt.subplots()

def animate(frame):

    global ax
    # code to set the limits of the axis
    ax.set_xlim(0, 720)
    ax.set_ylim(-1, 1)
    # setting x&y variables as the frame
    x = range(0, frame)
    x_in_radians = math.radians(x)
    y = math.sin(x_in_radians)
    #didn't need to do variables as counting frames, so could just put frame in. red circle marker.
    ax.plot(x[:frame], y[:frame])

def run():
    #referencing the global figure created above
    global fig

    # code for animation - calls the fig, the animate function, 10 frame and an interval of 1 second
    some_animation = animation.FuncAnimation(fig, animate, frames= 720, interval= 100)
    # code to show the subplot
    plt.show()





