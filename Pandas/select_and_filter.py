'''
This chapter is about extracting exactly the data you want from a DataFrame. We'll go slow
and layered, since it's one of the most used Pandas skills.
'''

from handle_csv import readCSVFromPath
import pandas as pd

def selectAndFilter() -> None:
    df: pd.DataFrame = readCSVFromPath()    # Retrieve a Pandas DataFrame object from a CSV file.
    emails: pd.Series = df["Email"]         # Get just an isolated column from the DatFrame object as Pandas Series object.

    print(f"type(emails): {type(emails)}")

    subset: pd.DataFrame = df[["Customer Id", "First Name", "Last Name"]]   # Get a DataFrame object from another (input a list of column names to "[]" operator).
    
    print(f"type(subset): {type(subset)}")

def main():
    selectAndFilter()

if __name__ == "__main__":
    main()