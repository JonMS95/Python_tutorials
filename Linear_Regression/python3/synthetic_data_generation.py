import numpy as np
import pandas as pd
from os import getcwd
from pathlib import Path, PosixPath
import matplotlib.pyplot as plt
import matplotlib.axes as axs
from data_logger import DataLogger

dlog: DataLogger = DataLogger()

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

    dlog.logInf(f"Generating linear data...")

    # Check whether provided boundaries have been properly established.
    if x_min >= x_max:
        raise ValueError("x_min must be strictly less than x_max")

    # Create random number generator (use provided seed).
    rng: np.random._generator.Generator = np.random.default_rng(random_state)

    # Create X-axis points.
    dlog.logDbg("Generating data points (X-axis)...")

    x: np.ndarray = rng.uniform(low = x_min, high = x_max, size = n_samples)

    # Based on X-axis data, generate a random Gaussian value for each point.
    dlog.logDbg("Generating random normal noise data points...")

    noise: np.ndarray = rng.normal(loc = 0.0, scale = noise_std, size = n_samples)

    # vectorization is used underneath: every element is operated element-wise.
    dlog.logDbg("Generating Y-axis data as f(x) = slope * x + intercept + noise...")
    
    y = slope * x + intercept + noise

    # Select some indices (from n_samples) so as to add outlier data points afterwards.
    dlog.logDbg("Generating outlier points...")
    
    n_outliers: int = int(outlier_ratio * n_samples)
    outlier_indices: np.ndarray = rng.choice(n_samples, size = n_outliers, replace = False)

    # For the outlier indices just picked up above, let's add abnormal noise values.
    y[outlier_indices] += rng.normal(loc = 0.0, scale = 10 * noise_std, size = n_outliers)

    # Add some missing entries.
    dlog.logDbg("Removing some data points in both axes...")

    n_missing: int = int(missing_ratio * n_samples) // 2 # Half for X, half for Y.
    x_missing_indices: np.ndarray = rng.choice(n_samples, size = n_missing, replace = False) 
    y_missing_indices: np.ndarray = rng.choice(n_samples, size = n_missing, replace = False)

    x[x_missing_indices] = np.nan
    y[y_missing_indices] = np.nan

    dlog.logInf("Generated random linear data including DataFrame.")

    return pd.DataFrame({"X" : x, "Y" : y })


def saveDataAsCSV(df: pd.DataFrame, save_csv_path: str = (getcwd() + "../../random_linear_data_dummy.csv")) -> None:
    """
    Save data (provided as Pandas DataFrame object) in a csv file. 

    Args:
        df              : Input Pandas DataFrame object.
        save_csv_path   : Target output csv file location.
    """

    dlog.logInf("Saving DataFrame object as .csv file...")

    path: PosixPath = Path(save_csv_path)

    if not path.parent.exists():
        raise ValueError(f"Provided path does not exist ({path})")

    df.to_csv(path, index = False)

    dlog.logInf(f"Saved DataFrame as {path.__str__}.")


def checkXYColumns(df: pd.DataFrame) -> None:
    """
    Checks whether expected columns (X and Y) are included in the DataFrame object. 
    Raises an exception if such condition is not met.
    
    Args:
        df              : Input Pandas DataFrame object.
    """

    if "X" not in df.columns or "Y" not in df.columns:
        raise ValueError("Column names do not match (\"X\", \"Y\")")
    
    if len(df.columns) > 2:
        raise ValueError(f"Found more columns than expected ({df.columns})")


def plotLinePlot(df: pd.DataFrame, save_plot: bool = False, display_plot: bool = True, plot_name: str = "noisy_linear_data_dummy.png") -> None:
    """
    Generate some random data for a linear function given a slope,
    an interceptor point and some noise parameters. 

    Args:
        df              : Input Pandas DataFrame object.
        save_plot       : T/F either to save the generated plot as png file or not.
        display_plot    : T/F either to display the generated plot or not.
    """

    checkXYColumns(df)

    dlog.logInf("Plotting data...")

    ax: axs = df.plot(  x = "X"                     ,
                        y = "Y"                     ,
                        kind = "scatter"            ,
                        title = "Noisy linear data" ,
                        grid = True                 ,
                        label = "Y"                 )

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.legend()

    plt.tight_layout()

    if save_plot:
        plt.savefig(plot_name)
        dlog.logInf(f"Saved data plot as {str(Path(plot_name).resolve())}")
    
    plt.show()


if __name__ == "__main__":
    plotLinePlot(generateLinearData(), save_plot = True, display_plot = False)