'''
Pandas can handle CSV files. In our case, we will be using a sample light database for such purpose.
A CSV file is nothing but a plain text file in which data is being separated by using newlines for rows
and commas for columns. It has no inherent types nor schema by nature. Therefore, when Pandas reads a
CSV file, it must parse text, infer structure, guess data types and normalize missing values. It's
worth pointing out that most bugs come from trusting these guesses blindly.
'''

import pandas as pd
import numpy as np
from pathlib import Path, PosixPath
from os import getcwd

nl: str = "\r\n"

def readCSVFromPath(csv_file_path: str = (getcwd() + "/test_data.csv")) -> pd.DataFrame:
    p: PosixPath = Path(csv_file_path)
    
    if not p.exists():
        raise FileNotFoundError(f"Target CSV file path does not exist ({csv_file_path})")

    df: pd.DataFrame = pd.read_csv(csv_file_path)   # Read from CSV and store it into a Dataframe object.
    df.drop(columns = ['Index'], inplace = True)    # Remove Index column (if any) since DataFrames generate their own by default.

    return df

def getDataFrameOverview(df: pd.DataFrame) -> None:
    print(f"First 5 rows, just for inspection purposes:{nl}{df.head()}{nl}")    # First 5 rows   
    print(f"Dataframe's dimensions:{nl}{df.shape}{nl}")                         # Numer of rows and columns (i.e., dimensions).
    print(f"Dataframe's column names:{nl}{df.columns.tolist()}{nl}")            # List of column names.
    print(f"Summary of data types and missing values:{nl}")                     # Get some basic information about the retrieved DataFrame.
    df.info(); print()
    print(f"Quick stats about the DataFrame object:{nl}{df.describe()}{nl}")    # Shows some generic data about the DataFrame in question.
    print(df.iloc[0])

def castToProperDataTypes(df: pd.DataFrame) -> None:
    cols_to_cast = [col for col in df.columns if col != 'Subscription Date']            # List of all columns except 'Subscription Date'.
    df[cols_to_cast] = df[cols_to_cast].astype(str)                                     # Cast all other columns to string.
    df['Subscription Date'] = pd.to_datetime(df['Subscription Date'], errors='coerce')  # Convert 'Subscription Date' to datetime

    # Should avoid casting each column manually as below:

    # df['Customer Id']       = df['Customer Id'].astype(str)
    # df['First Name']        = df['First Name'].astype(str)
    # df['Last Name']         = df['Last Name'].astype(str)
    # ...
    # ...
    # ...
    # df['Email']             = df['Email'].astype(str)
    # df['Subscription Date'] = df['Subscription Date'].astype(str)
    # df['Website']           = df['Website'].astype(str)

def addRandomBlankCells(df: pd.DataFrame, n_missing: int = 10, seed: int = 33) -> None:
    np.random.seed(seed)
    n_rows, n_cols = df.shape

    if n_missing > n_rows * n_cols:
        raise ValueError("Number of NaN values to introduce exceeds DataFrame object's boundaries")

    for _ in range(n_missing):
        row_idx: int = np.random.randint(0, n_rows)
        col_idx: int = np.random.randint(0, n_cols)
    
        df.iat[row_idx, col_idx] = np.nan

def solveMissingValues(df: pd.DataFrame) -> None:
    print(f"Number of NaN values per column:{nl}{df.isna().sum()}")
    # df.dropna(inplace = True)                     # Drop rows in which at least one column's value is NaN.
    # df.dropna(subset=['Email'], inplace = True)   # Drop rows with NaN in a specific column (not including a value in a given column may render the record useless).
    df.dropna(inplace = True)
    df.reset_index()                                # Reset index to keep it sequential.
    print(f"Number of NaN values per column (after dropna is executed for each record including at least a single NaN value):{nl}{df.isna().sum()}")

def main():
    df: pd.DataFrame = readCSVFromPath()
    getDataFrameOverview(df)
    castToProperDataTypes(df)
    addRandomBlankCells(df) # Add random NaN values since source CSV file has no blank cells.
    solveMissingValues(df)

if __name__ == "__main__":
    main()