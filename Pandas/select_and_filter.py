'''
This chapter is about extracting exactly the data you want from a DataFrame. We'll go slow
and layered, since it's one of the most used Pandas skills. This will work as a brush up for
other lessons.
'''

from handle_csv import readCSVFromPath, nl
import pandas as pd

def selectAndFilter() -> None:
    # Retrieve a Pandas DataFrame object from a CSV file.
    df: pd.DataFrame = readCSVFromPath()

    # Get just an isolated column from the DatFrame object as Pandas Series object.
    emails: pd.Series = df["Email"]
    print(f"type(emails): {type(emails)}")

    # Get a DataFrame object from another (input a list of column names to "[]" operator).
    subset: pd.DataFrame = df[["Customer Id", "First Name", "Last Name"]]
    print(f"type(subset): {type(subset)}")

    # DatafFrames can be amde of solely a single column.
    id: pd.DataFrame = df[["Customer Id"]]
    print(f"type(id): {type(id)}")

    # "iloc" stands for integer location (purely positional). Returns a row as a Pandas Series object if only a single row is selected. 
    first_row: pd.Series = df.iloc[0]
    print(f"type(first_row): {type(first_row)}")

    # "iloc" will return a DataFrame object is a slice ( [begin:end] ) is selected.
    first_five_rows: pd.DataFrame = df.iloc[0:5]
    print(f"type(first_five_rows): {type(first_five_rows)}")
    print(f"first_five_rows:{nl}{first_five_rows}")

    # Specific cells can be retrieved (also just numerically as the examples above) if a 2-element list is provided.
    cell: str = df.iloc[0, 2]
    print(f"cell at [0, 2]: {cell}")

    # Use "loc" to select more generic DataFrames.
    loc_data: pd.Series = df.loc[10]                                        # Solely 10th row.
    loc_data_row_and_col: pd.Series = df.loc[10, "Email"]                   # Selecting a single cell (10th row from "Email"-labeled column).
    loc_data_subset: pd.DataFrame = df.loc[0:4, ["Customer Id", "Email"]]   # Select a range of rows out of some selected columns.
    print(f"loc_data_subset (columns: {loc_data_subset.columns}, rows 0 to 4):{nl}{loc_data_subset}")

def main():
    selectAndFilter()

if __name__ == "__main__":
    main()