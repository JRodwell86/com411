import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()


def animate(frame):
    global ax
    # your code here (use ax to draw)
    ax.set_xlim(0, 10)
    ax.set_xlim(0, 10)
    x = [frame]
    y = [frame]
    ax.plot(x[:frame], y[:frame], 'ro')


def run():
    global fig
    # your code here (use fig with animation function)
    # code for animation - calls the fig, the animate function, 10 frame and an interval of 1 second
    some_animation = animation.FuncAnimation(fig, animate, frames=10, interval=1000)
    # code to show the subplot
    plt.show()


run()
