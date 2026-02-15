import pandas as pd
from synthetic_data_generation import checkXYColumns

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

    checkXYColumns(df)

    # Drop NaNs.
    df = df.dropna()

    # Remove outliers.
    y_mean  : float = df["Y"].mean()    # Dataset's mean value.
    y_std   : float = df["Y"].std()     # Standard deviation

    upper_bound : float = y_mean + 3 * y_std
    lower_bound : float = y_mean - 3 * y_std

    df = df[df["Y"].between(lower_bound, upper_bound)]

    return df