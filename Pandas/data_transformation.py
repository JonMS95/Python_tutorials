'''
This file will cover data transformation in Pandas. Topics to be covered include new column creation,
conditional columns, string transformations, applying custom logic and mapping values.
'''

import pandas as pd
from handle_csv import readCSVFromPath, nl

def creatingNewColumns(df: pd.DataFrame) -> None:
    # Import the DataFrame from a CSV file first.
    df: pd.DataFrame = readCSVFromPath()
    
    # In Pandas, loops are almost never used. Instead, entire columns are operated at once.
    df["Full Name"] = df["First Name"] + ' ' + df["Last Name"]

    df_full_name: pd.DataFrame = pd.DataFrame({
        "First Name": df["First Name"]  ,
        "Last Name" : df["Last Name"]   ,
        "Full Name" : df["Full Name"]   ,
    })
    print(f"df_full_name.head():{nl}{df_full_name.head()}")

def main():
    # Retrieve a Pandas DataFrame object from a CSV file.
    df: pd.DataFrame = readCSVFromPath()
    creatingNewColumns(df)

if __name__ == "__main__":
    main()