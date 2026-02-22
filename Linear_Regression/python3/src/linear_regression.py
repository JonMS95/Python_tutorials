'''
Provide a wrapper for C++ Least Squares method performing function.
'''

import sys
from pathlib import Path
import numpy as np
import pandas as pd
from synthetic_data_generation import generateLinearData
from data_preprocessing import preprocessData
from file_utils import checkXYColumns, saveDataAsCSV, loadDataFromCSV
from plotting import plotLinePlot
from data_logger import DataLogger
import pytest

# Ensure Python can find the shared C++ library
lib_path = (Path(__file__) / ".." / ".." / ".." / "cpp" / "lib").resolve()
sys.path.insert(0, str(lib_path))
import lib_cpp_linear_regression as cpp_lr


_dlog: DataLogger = DataLogger()


def fitLinearData1D(df: pd.DataFrame) -> tuple[float]:
    """
    Fit a line given a dataset. Use an external C++ function to do so.

    Args:
        df : Dataframe featuring the dataset to be fitted.
        
    Returns:
        A float tuple including intercept and slope, respectively.
    """
        
    checkXYColumns(df)

    _dlog.logInf("Getting optimal slope and interecept point from DataFrame via LS...")

    x: np.ndarray = df["X"].to_numpy(dtype=float)
    y: np.ndarray = df["Y"].to_numpy(dtype=float)

    intercept, slope = cpp_lr.fitLinearData(x, y)

    _dlog.logInf(f"After having performed Least Squares method, intercept: {intercept}, slope: {slope}")

    return (intercept, slope)


def test_perfect_line() -> None:
    """
    Check output value for a perfect line.
    """
    df = pd.DataFrame({
        "X": [0, 1, 2, 3],
        "Y": [1, 3, 5, 7]
    })

    intercept, slope = fitLinearData1D(df)

    assert abs(intercept-1) < 1e-6
    assert abs(slope-2) < 1e-6


def test_noisy_line() -> None:
    """
    Check that output for noisy line is found within expected boundaries.
    """
    rng = np.random.default_rng(0)
    x = np.linspace(0,10,100)
    y = 4*x+2+rng.normal(0,0.5,len(x))
    df = pd.DataFrame({"X":x,"Y":y})

    intercept,slope = fitLinearData1D(df)

    assert abs(slope-4)<0.2
    assert abs(intercept-2)<0.5


def test_missing_columns() -> None:
    """
    An exception must be raised if column names are not "X" and "Y".
    """
    df = pd.DataFrame({
        "A" : [1, 2],
        "B" : [3, 4]
    })

    with pytest.raises(Exception):
        fitLinearData1D(df)


def test_two_points() -> None:
    """
    Same as perfect line test for two data points.
    """
    df = pd.DataFrame({
        "X" : [0, 1],
        "Y" : [2, 4]
    })

    intercept,slope = fitLinearData1D(df)
    
    assert slope==2


def test_zero_variance() -> None:
    """
    Check that an error is raised for zero-variance datasets.
    """
    df = pd.DataFrame({"X":[1,1,1],"Y":[1,2,3]})
    
    with pytest.raises(RuntimeError):
        fitLinearData1D(df)


def _functionalTest() -> None:
    """
    Generate synthetic data, save it in a .csv file, load the
    dataframe from that .csv file, preprocess it, get the
    fitted line via Least Squares method and save a plot
    featuring the data.
    """

    _dlog.logInf("Generating testing synthetic data...")
    noisy_df: pd.DataFrame = generateLinearData()
    
    noisy_data_name : str = "noisy_linear_data_dummy"

    _dlog.logInf("Save generated synthetic data in a .csv file")
    csv_file_name: str = noisy_data_name + ".csv"
    saveDataAsCSV(noisy_df, csv_file_name)

    _dlog.logInf(f"Loading Pandas DataFrame object from {csv_file_name} file...")
    df: pd.DataFrame = loadDataFromCSV(csv_file_name)

    _dlog.logInf("Preprocessing data extracted from .csv file...")
    df = preprocessData(df)

    _dlog.logInf("Getting intercept and slope values by performing least squares method over extracted data...")
    b, m = fitLinearData1D(df)  # f(x) = m·x + b

    _dlog.logInf(f"Intercept: {b}, slope: {m}.")
    plot_file_name: str = "clean_linear_data_dummy_plus_LS.png"
    
    _dlog.logInf(f"Plot data: {plot_file_name}.")
    plotLinePlot(df         = df            ,
                 intercept  = b             ,
                 slope      = m             ,
                 plot_name  = plot_file_name)


if __name__ == "__main__":
    _functionalTest()
