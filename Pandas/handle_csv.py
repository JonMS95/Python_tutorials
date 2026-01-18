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

nl: str = "\r\n"

def readCSVFromPath(csv_file_path: str = (getcwd() + "/test_data.csv")) -> pd.DataFrame:
    p: PosixPath = Path(csv_file_path)
    
    if not p.exists():
        raise FileNotFoundError(f"Target CSV file path does not exist ({csv_file_path})")

    return pd.read_csv(csv_file_path)    

def getDataFrameOverview(df: pd.DataFrame) -> None:
    print(f"First 5 rows, just for inspection purposes:{nl}{df.head()}{nl}")    # First 5 rows   
    print(f"Dataframe's dimensions:{nl}{df.shape}{nl}")                         # Numer of rows and columns (i.e., dimensions).
    print(f"Dataframe's column names:{nl}{df.columns.tolist()}{nl}")            # List of column names.
    print(f"Summary of data types and missing values:{nl}")                     # Get some basic information about the retrieved DataFrame.
    df.info(); print()
    print(f"Quick stats about the DataFrame object:{nl}{df.describe()}{nl}")    # Shows some generic data about the DataFrame in question.

def main():
    df: pd.DataFrame = readCSVFromPath()
    getDataFrameOverview(df)

if __name__ == "__main__":
    main()