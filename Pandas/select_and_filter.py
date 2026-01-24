'''
This chapter is about extracting exactly the data you want from a DataFrame. We'll go slow
and layered, since it's one of the most used Pandas skills. This will work as a brush up for
other lessons.
'''

from handle_csv import readCSVFromPath, nl
import pandas as pd

def basicSelection(df: pd.DataFrame) -> None:
    # Get just an isolated column from the DatFrame object as Pandas Series object.
    emails: pd.Series = df["Email"]
    print(f"type(emails): {type(emails)}")

    # Get a DataFrame object from another (input a list of column names to "[]" operator).
    subset: pd.DataFrame = df[["Customer Id", "First Name", "Last Name"]]
    print(f"type(subset): {type(subset)}")

    # DatafFrames can be amde of solely a single column.
    id: pd.DataFrame = df[["Customer Id"]]
    print(f"type(id): {type(id)}")

def ilocUsage(df: pd.DataFrame) -> None:
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

def locUsage(df: pd.DataFrame) -> None:
    # Use "loc" to select more generic DataFrames.
    loc_data: pd.Series = df.loc[10]                                        # Solely 10th row.
    loc_data_row_and_col: pd.Series = df.loc[10, "Email"]                   # Selecting a single cell (10th row from "Email"-labeled column).
    loc_data_subset: pd.DataFrame = df.loc[0:4, ["Customer Id", "Email"]]   # Select a range of rows out of some selected columns.
    print(f"loc_data_subset (columns: {loc_data_subset.columns}, rows 0 to 4):{nl}{loc_data_subset}")

def booleanFiltering(df: pd.DataFrame) -> None:
    # Retrieve a subset DataFrame where Country's value is equal to Chile (equivalent to SQL's WHERE clause).
    chile_customers: pd.DataFrame = df[df["Country"] == "Chile"]
    print(f"chile_customers.head(): {chile_customers.head()}")

    # Multiple conditions can be used to filter. Take into account that every condition should be wrapped between parentheses.
    # Also, use '&', '|' , '~' instead of "AND", "OR", "NOT".
    dutch_new_members: pd.DataFrame = df[
        (df["Country"] == "Netherlands") &
        (df["Subscription Date"] > "2020-01-01")
    ]
    print(f"dutch_new_members: {dutch_new_members}")

    # A chunk of a string can be used to filter too (equivalent to SQL's LIKE clause) with .str.contains().
    org_dom_mail_users: pd.DataFrame = df[
        df["Email"].str.contains(".org", na=False) # Same as WHERE Email LIKE(%gmail%)
    ]
    print(f"gmail_users.head(): {org_dom_mail_users.head()}")

    # Use ~ to exclude results. Take into account that a DataFrame can be negated. Again, keep select clause between parentehses before applying ~.
    not_chilean_customers: pd.DataFrame = df[
        ~(df["Country"] == "Chile") # Flips True with False and viceversa.
    ]
    print(f"Not chilean customers (head): {not_chilean_customers.head()}")
    
    # Use isin.() to find whether a result is within a set of knwon values (equivalent to SQL's IN clause).
    chilean_dutch_and_moroccan_customers: pd.DataFrame = df[
        df["Country"].isin(["Chile", "Netherlands", "Morocco"])
    ]
    print(f"chilean_dutch_and_moroccan_customers:{nl}{chilean_dutch_and_moroccan_customers}")
 
    # ~ and | and/or .isin can be used to exclude by multiple criteria.
    not_albanian_nor_russian_customers: pd.DataFrame = df[
        ~(
            (df["Country"] == "Albania") |
            (df["Country"].str.contains("Russia", na = False))  # Reject treating "NaN" values (no string method exists for them).
        )
    ][["First Name", "Last Name", "Country"]]
    print(f"not_albanian_nor_russian_customers.head():{nl}{not_albanian_nor_russian_customers.head()}")
    
def selectAndFilter() -> None:
    # Retrieve a Pandas DataFrame object from a CSV file.
    df: pd.DataFrame = readCSVFromPath()

    basicSelection(df)
    ilocUsage(df)
    locUsage(df)
    booleanFiltering(df)

def main():
    selectAndFilter()

if __name__ == "__main__":
    main()