import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

MATRIX_LOW  = 0
MATRIX_HIGH = 2

MATRIX_ROWS = 5
MATRIX_COLS = 5

fig = plt.figure(figsize=(5, 5))

def update(frame):
    # Generate a random matrix of integers between 0 and 255
    matrix = np.random.randint(low=MATRIX_LOW, high=MATRIX_HIGH, size=(MATRIX_ROWS, MATRIX_COLS))

    plt.clf()

    # Plot the matrix as an image
    ax = plt.imshow(matrix, cmap='gray', interpolation='nearest', extent=[0, matrix.shape[1], 0, matrix.shape[0]])

    # Set the tick locations for the x and y axes to create a fixed grid
    ax.axes.set_xticks(np.arange(-0.5, matrix.shape[1], 1) + 0.5)
    ax.axes.set_yticks(np.arange(-0.5, matrix.shape[0], 1) + 0.5)

    # Remove the tick labels
    ax.axes.set_xticklabels([])
    ax.axes.set_yticklabels([])

    # Add a grid to the plot
    plt.grid(True, which='both', color='black', linestyle='-', linewidth=1)

    return ax

# Create an animation with 10 frames
anim = FuncAnimation(fig, update, frames=10, interval=500, repeat=False)

plt.show()
