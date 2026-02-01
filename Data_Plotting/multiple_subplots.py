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

def main():
    pass

if __name__ == "__main__":
    main()