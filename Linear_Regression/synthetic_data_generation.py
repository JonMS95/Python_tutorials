import numpy as np
import pandas as pd
from os import getcwd
from pathlib import Path, PosixPath
import matplotlib.pyplot as plt
import matplotlib.axes as axs

def generateLinearData( n_samples       : int   = 500   ,
                        slope           : float = 3.0   ,
                        intercept       : float = 7.0   ,
                        x_min           : float = -10.0 ,
                        x_max           : float = 10.0  ,
                        noise_std       : float = 1.0   ,
                        outlier_ratio   : float = 0.02  ,
                        missing_ratio   : float = 0.02  ,
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
        A noisy linear function (ax + b + N(x)) as a Pandas DataFrame object.
    """

    # Check whether provided boundaries have been properly established.
    if x_min >= x_max:
        raise ValueError("x_min must be strictly less than x_max")

    # Create random number generator (use provided seed).
    rng: np.random._generator.Generator = np.random.default_rng(random_state)

    # Create X-axis points.
    x: np.ndarray = rng.uniform(low = x_min, high = x_max, size = n_samples)

    # Based on X-axis data, generate a random Gaussian value for each point.
    noise: np.ndarray = rng.normal(loc = 0.0, scale = noise_std, size = n_samples)

    # vectorization is used underneath: every element is operated element-wise.
    y = slope * x + intercept + noise

    # Select some indices (from n_samples) so as to add outlier data points afterwards.
    n_outliers: int = int(outlier_ratio * n_samples)
    outlier_indices: np.ndarray = rng.choice(n_samples, size = n_outliers, replace = False)

    # For the outlier indices just picked up above, let's add abnormal noise values.
    y[outlier_indices] += rng.normal(loc = 0.0, scale = 10 * noise_std, size = n_outliers)

    # Add some missing entries.
    n_missing: int = int(missing_ratio * n_samples) // 2 # Half for X, half for Y.
    x_missing_indices: np.ndarray = rng.choice(n_samples, size = n_missing, replace = False) 
    y_missing_indices: np.ndarray = rng.choice(n_samples, size = n_missing, replace = False)

    x[x_missing_indices] = np.nan
    y[y_missing_indices] = np.nan

    return pd.DataFrame({"X" : x, "Y" : y })

def saveDataAsCSV(df: pd.DataFrame, save_csv_path: str = (getcwd() + "/random_linear_data_dummy.csv")) -> None:
    """
    Save data (provided as Pandas DataFrame object) in a csv file. 

    Args:
        df              : Input Pandas DataFrame object.
        save_csv_path   : Target output csv file location.
    """

    path: PosixPath = Path(save_csv_path)

    if not path.parent.exists():
        raise ValueError(f"Provided path does not exist ({path})")

    df.to_csv(path, index = False)

