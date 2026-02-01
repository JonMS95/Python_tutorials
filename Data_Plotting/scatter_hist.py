'''
This file is an extension of "basic_plots.py", it's not meant to reinvent anything.
Scatter plots and histograms will be introduced.
'''

import matplotlib
matplotlib.use("TkAgg")  # Must be before pyplot
import matplotlib.pyplot as plt
import numpy as np

def dataGeneration(seed_value: int = 42) -> tuple[np.ndarray]:
    # Fix a random number generator, ensuring reproducibility.
    np.random.seed(seed_value)
    
    # Generate data.
    x: np.ndarray = np.linspace(0, 10, 100)                                     # Generate 100 evenly spaced points from 0 to 10.
    y: np.ndarray = np.sin(x) + np.random.normal(scale = 0.2, size = len(x))    # Clean signal (sin(x)) plus Gaussian noise, where scale is noise magnitude, and size is one per sin(x) point.
    z: np.ndarray = np.random.normal(loc = 0, scale = 1, size = 1_000)          # loc for mean value, scale for standard deviation.

    return (x, y, z)

def plotScatterData(x: np.ndarray, y: np.ndarray) -> None:
    fig, ax = plt.subplots(figsize = (8, 4))

    # Different from .plot(), .scatter() draws points, not lines.
    ax.scatter(x                        ,   # x axis
               y                        ,   # y axis
               color = "purple"         ,   # data points color
               alpha = 0.6              ,   # transparency
               s = 40                   ,   # marker size (area, not radius)
               label = "Noisy sin(x)"   )   # legend entry
    
    ax.set_title("Scatter plot: relationship between variables")
    ax.set_xlabel("X values")
    ax.set_ylabel("Y values")
    ax.legend()
    ax.grid(True)

    fig.tight_layout()
    # fig.savefig("scatter_plot.png")
    plt.show()

def main():
    data: tuple[np.ndarray] = dataGeneration()
    plotScatterData(data[0], data[1])

if __name__ == "__main__":
    main()