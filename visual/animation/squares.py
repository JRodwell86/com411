import matplotlib.pyplot as plt
import matplotlib.animation as animation
# creating the figure and the subplot
fig, ax = plt.subplots()

squares = []

def init():
    global squares
    small = {"x": [3, 3, 4, 4, 3], "y": [3, 4, 4, 3, 3]}
    medium = {"x": [2, 5, 5, 2, 2], "y": [2, 2, 5, 5, 2]}
    large = {"x": [1, 6, 6, 1, 1], "y": [1, 1, 6, 6, 1]}
    squares.append(small)
    squares.append(medium)
    squares.append(large)

def animate(frame):
    global ax
    #code to plot the squares - load by frame and then access the dictionary frame by frame through [] and letter.
    ax.plot(squares[frame]["x"], squares[frame]["y"])



def run():
    init()
    some_animation = animation.FuncAnimation(fig, animate, frames=3, interval=1000, repeat =True)
    plt.show()


run()

print(squares)