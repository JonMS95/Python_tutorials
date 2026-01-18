'''
Pandas can handle CSV files. In our case, we will be using a sample light database for such purpose.
A CSV file is nothing but a plain text file in which data is being separated by using newlines for rows
and commas for columns. It has no inherent types nor schema by nature. Therefore, when Pandas reads a
CSV file, it must parse text, infer structure, guess data types and normalize missing values. It's
worth pointing out that most bugs come from trusting these guesses blindly.
'''

import pandas as pd
from pathlib import Path, PosixPath
from os import getcwd

def readCSVFromPath(csv_file_path: str = (getcwd() + "/test_data.csv")) -> pd.DataFrame:
    p: PosixPath = Path(csv_file_path)
    
    if not p.exists():
        raise FileNotFoundError(f"Target CSV file path does not exist ({csv_file_path})")

    return pd.read_csv(csv_file_path)    

def getDataFrameOverview(df: pd.DataFrame) -> None:
    print(f"First 5 rows, just for inspection purposes:\r\n {df.head()}")   # First 5 rows   
    print(f"Dataframe's dimensions: {df.shape}")                            # Numer of rows and columns (i.e., dimensions).
    print(f"Dataframe's column names:{df.columns.tolist()}")                # List of column names.

def main():
    df: pd.DataFrame = readCSVFromPath()
    getDataFrameOverview(df)

if __name__ == "__main__":
    main()