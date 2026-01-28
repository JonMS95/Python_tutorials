'''
This file will cover data transformation in Pandas. Topics to be covered include new column creation,
conditional columns, string transformations, applying custom logic and mapping values.
'''

import pandas as pd
import numpy as np
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

def conditionalColumns(df: pd.DataFrame) -> None:
    # Columns can be created conditionally.
    df["Is Europe"] = df["Country"].isin(["Spain", "France", "Germany", "Italy", "Monaco", "Switzerland", "Poland"])   # There are more countries in Europe but this just an example.

    # Create a new df by selecting the rows in which "Is Europe" is True. Note that it's different from df["Is Europe"], which just selects a column.
    european_customers: pd.DataFrame = df[df["Is Europe"]]
    # It's equivalent to the statements below:
    # df_european_customers: pd.DataFrame = df.iloc[df["Is Europe"]]
    # df_european_customers: pd.DataFrame = df[df["Is European"] == True]
    # Keep in mind that [] operator is equivalent to "where".

    df_new_european_customers: pd.DataFrame = pd.DataFrame({
        "Country"   : european_customers["Country"],
        "Full Name" : (european_customers["First Name"] + ' ' + european_customers["Last Name"]),
    })

    print(f"df_european_countries.head():{nl}{df_new_european_customers.head()}")

    # New columns can be created based on numeric/date-based condition.
    df["Subscription Date"] = pd.to_datetime(df["Subscription Date"])
    df["Is Recent"] = df["Subscription Date"] >= "2021-01-01"    # Equivalent to saying: new column namely "Is Recent" is equivalent to bool column where value is true for rows in which
                                                                #subscription date is more recent than 2021.

    # Multiple conditions can be used to generate new columns.
    df["EU Recent"] = df["Is Europe"] & df["Is Recent"] # This will generate a bool column equivalent to "Is Europe" & "Is Recent" per row.
    
    eu_recent: pd.DataFrame = df[df["EU Recent"]]   # Select only rows in which "EU Recent" is True, make a new dataframe out of those rows.
    eu_recent = pd.DataFrame({
        "Country"           : eu_recent["Country"]          ,
        "Subscription Date" : eu_recent["Subscription Date"],
    })

    print(f"eu_recent.head():{nl}{eu_recent.head()}")

def main():
    # Retrieve a Pandas DataFrame object from a CSV file.
    df: pd.DataFrame = readCSVFromPath()
    creatingNewColumns(df)
    conditionalColumns(df)

if __name__ == "__main__":
    main()