'''
This is an introductory lesson about matplotlib. Simple examples featuring simple lines will be included here.

Commands below may be required:
pip install Pillow
sudo apt install python3-tk
'''

import matplotlib
matplotlib.use("TkAgg")  # Forces an interactive GUI backend. Must be before pyplot.
import matplotlib.pyplot as plt
import numpy as np

def quickPlotting(x: np.ndarray, y0: np.ndarray, y1: np.ndarray) -> None:
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

def plotWithAPI(x: np.ndarray, y0: np.ndarray, y1: np.ndarray) -> None:
    # Creates both a figure (like a canvas, containing axes, titles and plots) and ax (axes) is where the actual plot lives in.
    # Axes objects are where each plot live, while Fugure objects are where plots, titles and everything that wraps them is included.
    fig, ax = plt.subplots(figsize = (8, 4))
    
    # Plot both functions.
    ax.plot(x, y0, label = "sin(x)", color = "green", linestyle = "-", marker = "o", markersize = 4)
    ax.plot(x, y1, label = "cos(x)", color = "orange", linestyle = "--", marker = "x", markersize = 4)
    
    # Add some legend to the plot and render it.
    ax.set_title("OO API Line Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.legend()
    ax.grid(True)
    fig.tight_layout()
    # fig.savefig("line_plot_oo.png")   # Uncomment to save generated plot as png file.
    plt.show()

def dummyExample() -> None:
    # Generate data to be plotted.
    x: np.ndarray   = np.linspace(0, 10, 100)   # Generate 100 evenly spaced data points from 0 to 10.
    y0: np.ndarray  = np.sin(x)                 # Execute sine function over points generated above.
    y1: np.ndarray  = np.cos(x)                 # Same for cosine function.

    # There are two main way make a plot: quick and API.
    quickPlotting(x, y0, y1)
    plotWithAPI(x, y0, y1)

def main():
    dummyExample()

if __name__ == "__main__":
    main()