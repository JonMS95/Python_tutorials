'''
Multiple subplots can be rendered within the same figure using Matplotlib's OO API.
'''

import matplotlib
matplotlib.use("TkAgg")  # Must be before pyplot
import matplotlib.pyplot as plt
import numpy as np

def generateData() -> tuple[np.ndarray]:
    x       : np.ndarray = np.linspace(0, 10, 100)
    y_sin   : np.ndarray = np.sin(x)
    y_cos   : np.ndarray = np.cos(x)
    y_noise : np.ndarray = np.sin(x) + np.random.normal(scale = 0.2, size = len(x)) # Create a sin(x) function plus some random data with as many points as x axis.

    return (x, y_sin, y_cos, y_noise)

def createSubplots(data: tuple[np.ndarray]) -> None:
    fig, axs = plt.subplots(nrows = 2           ,   # 2 rows and 2 columns, since 4 plots are going to be shown.
                            ncols = 2           ,   # (axs is a 2x2 array of axes objects)
                            figsize = (10, 6)   ,
                            sharex = True       ,   # All subplots use the same x-axis limits and ticks.
                            sharey = False      )   # All subplots use their own y_axis and ticks.

    # Upper-left
    axs[0, 0].plot(data[0], data[1], color = "blue")
    axs[0, 0].set_title("sin(x)")
    axs[0, 0].grid(True)

    # Upper-right
    axs[0, 1].plot(data[0], data[2], color = "green")
    axs[0, 1].set_title("cos(x)")
    axs[0, 1].grid(True)

    # Down-left
    axs[1, 0].scatter(data[0], data[3], color = "purple")
    axs[1, 0].set_title("Noisy sin(x)")
    axs[1, 0].grid(True)
    
    # Down-right
    axs[1, 1].hist(data[3], bins = 30, color = "steelblue", edgecolor = "black")
    axs[1, 1].set_title("Distribution of noisy sin(x)")
    axs[1, 1].grid(axis = "y")

    fig.suptitle("Multiple subplots example", fontsize = 14)
    fig.tight_layout()  # Automatically adjust spacing between subplot(s) so that axis and tick labels nor titles overlap.
    # fig.savefig("multiple_subplots.png")
    plt.show()

def main():
    createSubplots(generateData())

if __name__ == "__main__":
    main()