'''
Generate synthetic data (linear data + Gaussian noise).
'''

import numpy as np
import pandas as pd
from data_logger import DataLogger
import pytest
from file_utils import saveDataAsCSV
from plotting import plotLinePlot


_dlog : DataLogger = DataLogger()


def generateLinearData( n_samples       : int   = 100   ,
                        slope           : float = 3.0   ,
                        intercept       : float = 7.0   ,
                        x_min           : float = -10.0 ,
                        x_max           : float = 10.0  ,
                        noise_std       : float = 10.0  ,
                        outlier_ratio   : float = 0.05  ,
                        missing_ratio   : float = 0.05  ,
                        random_state    : int   = 33    ) -> pd.DataFrame:
    """
    Generate some random data for a linear function given a slope,
    an interceptor point and some noise parameters. 

    Args:
        n_samples       : Number of samples.
        slope           : Line's slope.
        intercept       : Intercepting point (function's value when x = 0).
        x_min           : Minimum X-axis value.
        x_max           : Maximum X-axis value.
        noise_std       : Standard deviation of Gaussian noise added to y-axis.
        outlier_ratio   : Fraction of samples whose target y is heavily perturbed.
        missing_ratio   : Fraction of values replaced with NaN.
        random_state    : Seed for reproducibility matters.
        
    Returns:
        A noisy linear function (f(x) = ax + b + N(x)) as a Pandas DataFrame object.
    """

    _dlog.logInf(f"Generating linear data...")

    # Check whether provided boundaries have been properly established.
    if x_min >= x_max:
        raise ValueError("x_min must be strictly less than x_max")

    # Create random number generator (use provided seed).
    rng: np.random._generator.Generator = np.random.default_rng(random_state)

    # Create X-axis points.
    _dlog.logDbg("Generating data points (X-axis)...")

    x: np.ndarray = rng.uniform(low = x_min, high = x_max, size = n_samples)

    # Based on X-axis data, generate a random Gaussian value for each point.
    _dlog.logDbg("Generating random normal noise data points...")

    noise: np.ndarray = rng.normal(loc = 0.0, scale = noise_std, size = n_samples)

    # vectorization is used underneath: every element is operated element-wise.
    _dlog.logDbg("Generating Y-axis data as f(x) = slope * x + intercept + noise(x)...")
    
    y = slope * x + intercept + noise

    # Select some indices (from n_samples) so as to add outlier data points afterwards.
    _dlog.logDbg("Generating outlier points...")
    
    n_outliers: int = int(outlier_ratio * n_samples)
    outlier_indices: np.ndarray = rng.choice(n_samples, size = n_outliers, replace = False)

    # For the outlier indices just picked up above, let's add abnormal noise values.
    y[outlier_indices] += rng.normal(loc = 0.0, scale = 10 * noise_std, size = n_outliers)

    # Add some missing entries.
    _dlog.logDbg("Removing some data points in both axes...")

    n_missing: int = int(missing_ratio * n_samples) // 2 # Half for X, half for Y.
    x_missing_indices: np.ndarray = rng.choice(n_samples, size = n_missing, replace = False) 
    y_missing_indices: np.ndarray = rng.choice(n_samples, size = n_missing, replace = False)

    x[x_missing_indices] = np.nan
    y[y_missing_indices] = np.nan

    _dlog.logInf("Generated random linear data including DataFrame.")

    return pd.DataFrame({"X" : x, "Y" : y })


def test_returns_dataframe() -> None:
    """
    Test basic functionality.
    """
    df = generateLinearData(n_samples=50)
    assert isinstance(df, pd.DataFrame)
    assert list(df.columns) == ["X", "Y"]
    assert len(df) == 50


def test_x_min_less_than_x_max() -> None:
    """
    Test boundary values.
    """
    with pytest.raises(ValueError):
        generateLinearData(x_min=5, x_max=5)

def test_random_seed_reproducibility() -> None:
    """
    Test random seed's reproducibility (same output for equal seeds).
    """
    df1 = generateLinearData(random_state=123)
    df2 = generateLinearData(random_state=123)
    pd.testing.assert_frame_equal(df1, df2)


def test_linear_relationship_with_noise() -> None:
    """
    Test linear relationship with noise.
    """
    slope = 2.0
    intercept = 5.0
    noise_std = 3.0
    df = generateLinearData(n_samples=100, slope=slope, intercept=intercept, noise_std=noise_std, outlier_ratio=0, missing_ratio=0, random_state=42)
    
    residuals = df["Y"] - (slope * df["X"] + intercept)
    
    # Check mean close to 0
    assert abs(residuals.mean()) < 1.0
    
    # Check std roughly equals noise_std (allow some tolerance)
    assert abs(residuals.std() - noise_std) < 1.0


def test_missing_values_count() -> None:
    """
    Test missing value insertion.
    """
    n_samples = 100
    missing_ratio = 0.1
    df = generateLinearData(n_samples=n_samples, missing_ratio=missing_ratio, random_state=42)
    
    expected_missing = int(missing_ratio * n_samples) // 2
    assert df["X"].isna().sum() == expected_missing
    assert df["Y"].isna().sum() == expected_missing


def test_zero_samples() -> None:
    """
    Test edge case n_samples=0:
    """
    df = generateLinearData(n_samples=0)
    assert df.empty


def test_no_outliers_no_missing() -> None:
    """
    Test edge case with no outliers and no missing values:
    """
    df = generateLinearData(n_samples=50, outlier_ratio=0, missing_ratio=0)
    assert not df.isna().any().any()

    # Rough check that all values are close to line (allow some noise)
    residuals = df["Y"] - (3.0 * df["X"] + 7.0)
    assert all(abs(residuals) < 50)


def test_column_dtypes() -> None:
    """
    Test that the returned DataFrame columns are numeric.
    """
    df = generateLinearData(n_samples=10)
    assert df["X"].dtype == float
    assert df["Y"].dtype == float


def _functionalTest() -> None:
    """
    Generate synthetic data and store it in a CSV file.
    Plot it afterwards.
    """
    _dlog.logInf("Generating testing synthetic data...")
    df: pd.DataFrame = generateLinearData()

    noisy_data_name : str = "noisy_linear_data_dummy"

    _dlog.logInf(f"Saving testing data in {noisy_data_name + '.csv'}")
    saveDataAsCSV(df, noisy_data_name + ".csv")

    _dlog.logInf(f"Plot testing data in {noisy_data_name + '.png'}")
    plotLinePlot(df, plot_name = noisy_data_name + '.png')


if __name__ == "__main__":
    _functionalTest()
