import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import GameOfLife as gol

MATRIX_LOW  = 0
MATRIX_HIGH = 2

MATRIX_ROWS = 10
MATRIX_COLS = 10

matrix = gol.GameOfLife(MATRIX_ROWS, MATRIX_COLS)
fig = plt.figure(figsize=(MATRIX_ROWS, MATRIX_COLS))

def update(frame):
    plt.clf()

    currentBoard = matrix.getNextBoardState()

    # Plot the matrix as an image
    ax = plt.imshow(currentBoard, cmap='gray_r', interpolation='nearest', extent=[0, matrix.getBoardSize()[1], 0, matrix.getBoardSize()[0]])

    # Set the tick locations for the x and y axes to create a fixed grid
    ax.axes.set_xticks(np.arange(-0.5, matrix.getBoardSize()[1], 1) + 0.5)
    ax.axes.set_yticks(np.arange(-0.5, matrix.getBoardSize()[0], 1) + 0.5)

    # Remove the tick labels
    ax.axes.set_xticklabels([])
    ax.axes.set_yticklabels([])

    # Add a grid to the plot
    plt.grid(True, which='both', color='black', linestyle='-', linewidth=1)

    return ax

# Create an animation with 10 frames
anim = FuncAnimation(fig, update, frames=100, interval=500, repeat=False)

plt.show()
