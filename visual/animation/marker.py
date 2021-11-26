import matplotlib.pyplot as plt
import matplotlib.animation as animation
# creating the figure and the subplot
fig, ax = plt.subplots()

#def init():
    #global ax
    # code to set the limits of the axis

    #ax.set_xlim(0, 10)
    #ax.set_ylim(0, 10)


def animate(frame):

    global ax
    #code to clear the previous plot at the start of every animation loop
    ax.cla()
    # code to set the limits of the axis
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    # setting x&y variables as the frame
    x = [frame]
    y = [frame]
    #didn't need to do variables as counting frames, so could just put frame in. red circle marker.
    ax.plot(x[:frame], y[:frame], 'ro')



def run():
    #referencing the global figure created above
    global fig

    # code for animation - calls the fig, the animate function, 10 frame and an interval of 1 second
    some_animation = animation.FuncAnimation(fig, animate, frames= 10, interval= 1000)
    # code to show the subplot
    plt.show()


run()