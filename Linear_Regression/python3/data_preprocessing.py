import pandas as pd
import numpy as np
from synthetic_data_generation import checkXYColumns, generateLinearData, plotLinePlot
from data_logger import DataLogger

dlog: DataLogger = DataLogger()

def preprocessData(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns clean dataset taking given dataframe by removing:
        ·Outlier points following 3σ rule (an empirical rule which assumes that 99.7% of the data falls within three standard deviations). 
        ·Missing data.
    
    Args:
        df  : Pandas DataFrame object.
        
    Returns:
        Clean dataset as a Pandas DataFrame object.
    """

    dlog.logInf(f"Preprocessing data...")

    checkXYColumns(df)

    # Drop NaNs (.dropna removes the whole row in case any of the values within the row is NaN).
    dlog.logDbg(f"Removing rows with NaN values...")

    df = df.dropna()

    # Remove outliers.
    dlog.logDbg(f"Removing outlier data points (following 3σ rule)...")
    
    y_mean  : float = df["Y"].mean()    # Dataset's mean value.
    y_std   : float = df["Y"].std()     # Standard deviation

    upper_bound : float = y_mean + 3 * y_std
    lower_bound : float = y_mean - 3 * y_std

    filter: pd.DataFrame = df["Y"].between(lower_bound, upper_bound)    # Retrieves solely the rows where data is found between specified limits as bool mask.
    df = df[filter] # Equivalent to selecting rows from given DataFrame where data is between lower and upper bounds.  

    return df


def test_returns_dataframe():
    """
    Test basic functionality.
    """
    df = generateLinearData(n_samples=50, missing_ratio=0.1, outlier_ratio=0.1, random_state=42)
    df_clean = preprocessData(df)

    assert isinstance(df_clean, pd.DataFrame)
    assert list(df_clean.columns) == ["X", "Y"]
    assert len(df_clean) <= len(df)


def test_removes_nan_rows():
    """
    Test that all rows with NaNs are removed.
    """
    df = pd.DataFrame({
        "X": [1.0, 2.0, np.nan, 4.0],
        "Y": [5.0, np.nan, 7.0, 8.0]
    })

    df_clean = preprocessData(df)

    # Only rows without NaNs remain.
    assert df_clean.isna().sum().sum() == 0

    # Only rows 0 and 3 remain.
    assert df_clean.shape[0] == 2
    assert df_clean.iloc[0]["X"] == 1.0
    assert df_clean.iloc[1]["X"] == 4.0


def test_empty_dataframe():
    """
    Test preprocessing on an empty DataFrame.
    """
    df_empty = pd.DataFrame(columns=["X", "Y"])
    df_clean = preprocessData(df_empty)
    
    assert df_clean.empty


def test_column_types_preserved():
    """
    Test that X and Y columns remain numeric after preprocessing.
    """
    df = generateLinearData(n_samples=20, missing_ratio=0.1, outlier_ratio=0.1, random_state=42)
    df_clean = preprocessData(df)

    assert df_clean["X"].dtype == float
    assert df_clean["Y"].dtype == float


if __name__ == "__main__":
    plotLinePlot(preprocessData(generateLinearData()), save_plot = True, display_plot = False, plot_name = "noisy_linear_data_clean_dummy.png")