'''
This is an introductory lesson about matplotlib. Simple examples featuring simple lines will be included here.

Commands below may be required:
pip install Pillow
sudo apt install python3-tk
'''

import matplotlib
matplotlib.use("TkAgg")  # Must be before pyplot
import matplotlib.pyplot as plt
import numpy as np

def dummyExample() -> None:
    # Generate data to be plotted.
    x: np.ndarray   = np.linspace(0, 10, 100)   # Generate 100 evenly spaced data points from 0 to 10.
    y0: np.ndarray  = np.sin(x)                 # Execute sine function over points generated above.
    y1: np.ndarray  = np.cos(x)                 # Same for cosine function.

    # Create a figure for plotting
    plt.figure(figsize = (8, 4))    # Width: 8, Height: 4 (both in inches!).

    # Plot both functions.
    plt.plot(x, y0, label = "sin(x)", color = "blue", linestyle = "-", marker = "o", markersize = 3)
    plt.plot(x, y1, label = "cos(x)", color = "red", linestyle = "--", marker = "x", markersize = 3)

    # Add some legend to the plot and render it.
    plt.title("Quick line plot")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    # plt.savefig("line_plot_quick.png")    # Uncomment to save generated plot as png file.
    plt.show()

def main():
    dummyExample()

if __name__ == "__main__":
    main()