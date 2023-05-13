import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import GameOfLife as gol
import argparse

MATRIX_LOW  = 0
MATRIX_HIGH = 2

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("-r", "--rows", default=10, type=int, help="Number of rows")
parser.add_argument("-c", "--columns", default=10, type=int, help="Number of columns")
parser.add_argument("-l", "--loop", default=False, action="store_true", help="Loop through X and Y axes when looking for adjacent cells")
parser.add_argument("-f", "--frames", default=100, type=int, help="Number of frames in the generated animation")
parser.add_argument("-m", "--milliseconds", default=500, type=int, help="Milliseconds from one animation frame until the next one")

args = parser.parse_args()

MATRIX_ROWS = args.rows
MATRIX_COLS = args.columns
LOOP_CELLS = args.loop

matrix = gol.GameOfLife(MATRIX_ROWS, MATRIX_COLS, LOOP_CELLS)
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
