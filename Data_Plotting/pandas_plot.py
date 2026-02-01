'''
This file shows how Pandas sits on top of Matplotlib, when it's useful, and what its limits are.
'''

import matplotlib
matplotlib.use("TkAgg")  # Must be before pyplot
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def generateDataFrame() -> pd.DataFrame:
    # Generate a sequence of 100 timestamps, one per day, starting on the first day of 2024.
    dates: pd.DatetimeIndex = pd.date_range(start = "2024-01-01", periods = 100, freq = "D")
    
    # Create an array of values as long as the priorly created list of timestamps.
    # Each value within the list is the previous value (if any) plus a random step.
    values: np.ndarray = np.cumsum(np.random.normal(scale = 1.0, size = len(dates)))

    df: pd.DataFrame = pd.DataFrame({
        "Date"  : dates,
        "value" : values
    })

    df.set_index("Date", inplace = True)    # Set dates as index inplace so that the DataFrame itself is modified.

def main():
    pass

if __name__ == "__main__":
    main()