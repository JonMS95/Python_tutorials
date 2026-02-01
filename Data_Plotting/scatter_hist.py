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
    x: np.ndarray = np.linspace(0, 100, 10)                                     # Generate 100 evenly spaced points from 0 to 10.
    y: np.ndarray = np.sin(x) + np.random.normal(scale = 0.2, size = len(x))    # Clean signal (sin(x)) plus Gaussian noise, where scale is noise magnitude, and size is one per sin(x) point.
    z: np.ndarray = np.random.normal(loc = 0, scale = 1, size = 1_000)          # loc for mean value, scale for standard deviation.

    return (x, y, z)

def main():
    pass

if __name__ == "__main__":
    main()