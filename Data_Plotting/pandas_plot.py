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
        "Value" : values
    })

    df.set_index("Date", inplace = True)    # Set dates as index inplace so that the DataFrame itself is modified.

    return df

def plotPandasLinePlot(df: pd.DataFrame) -> None:
    if "Value" not in df.columns:
        raise ValueError("Column labeled as \"Value\" was not found")

    # Pandas module includes a method (.plot()) that returns a matplotlib Axes object.
    ax: matplotlib.axes = df["Value"].plot( figsize = (8, 4)                      ,
                                            title = "Time series plot (Pandas)"   ,
                                            grid = True                           ,
                                            label = "Value"                       )

    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    ax.legend()

    plt.tight_layout()
    # plt.savefig("pandas_line_plit.png")
    plt.show()

def plotPandasHistogram(df: pd.DataFrame) -> None:
    if "Value" not in df.columns:
        raise ValueError("Column labeled as \"Value\" was not found")

    ax = df["Value"].plot(figsize = (8, 4)              ,
                          kind = "hist"                 ,
                          bins = 30                     ,
                          title = "Histogram (Pandas)"  ,
                          grid = True                   )
    
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")

    plt.tight_layout()
    # plt.savefig("pandas_histogram.png")
    plt.show()

def main():
    df: pd.DataFrame = generateDataFrame()
    plotPandasLinePlot(df)
    plotPandasHistogram(df)

if __name__ == "__main__":
    main()