'''
This file will show some examples so as to understand Pandas basics.
'''

import pandas as pd
import numpy as np

nl: str = "\r\n"
endl: str = 2 * nl

def pandasBasics() -> None:
    # Series: 1D labeled array.
    s = pd.Series([10, 20, 30], index = ['a', 'b', 'c'])    # index tells how each column is labeled.
    print(s, end = endl)

    # DataFrame: 2D labeled structure (like a table).
    data = {
        "Name":     ["Alice", "Bob", "Charlie", "Damon", "Elizabeth", "Frida"]  ,
        "Age":      [25, 31, 33, 19, 29, 40]                                    ,
        "Salary":   [70000, 80000, 90000, 30000, 55000, 100000]                 ,
    }
    df = pd.DataFrame(data)
    print(df, end = endl)
    
    # Viewing and inspecting data.
    print(f"df.head(): {df.head()}", end = endl)            # Retrieves first 5 rows by default, any number can be provided as longs as it complies with dataframe's dimensions.
    print(f"df.tail(3): {df.tail(3)}", end = endl)          # Sames as the prior method but with last instead of first rows.
    print(f"df.shape: {df.shape}", end = endl)              # Dimensions (rows, columns...).
    print(f"df.info(): {df.info()}", end = endl)            # Summary info.
    print(f"df.describe(): {df.describe()}", end = endl)    # Statistics for numeric columns. 
    print(f"df.columns: {df.columns}", end = endl)          # List of columns.
    print(f"df.index: {df.index}", end = endl)              # Row labels.

    # Selecting and filtering.
    print(f"df['Name']{nl}", df['Name'], end = endl)                                        # Single column (Series).
    print(f"df[['Name', 'Age']]{nl}", df[['Name', 'Age']], end = endl)                      # Multiple columns (DataFrame).
    print(f"df.iloc[0]{nl}", df.iloc[0], end = endl)                                        # First row ("iloc" is short for "integer location").
    print(f"df.iloc[0, 1]{nl}", df.iloc[0, 1], end = endl)                                  # Single cell.
    print(f"df[df['Age'] > 28]{nl}", df[df['Age'] > 28], end = endl)                        # Filter rows.
    print(f"df['Name'].str.contains('a'){nl}", df['Name'].str.contains('a'), end = endl)    # String filtering.

    # Adding/modifying columns.
    df['Bonus'] = df['Salary'] * 0.1                                    # Creates a new column multiplying every row by 0.1.
    df['AgeGroup'] = np.where(df['Age'] < 30, 'Young', 'Experienced')   # For every row, assign a value depending on "Age" column's values rows (np.where returns an array of elements matching specified criteria).
    print(f"df['Bonus']: {df['Bonus']}")
    print(f"df['AgeGroup']: {df['AgeGroup']}")

    # Handling missing data.
    df['Salary'].fillna(df['Salary'].mean(), inplace = True)    # Replace every blank (NaN, None) cell of Salary column with the column's average.
    df.dropna(inplace = True)                                   # Removes entire rows containing at least one NaN. Axis can be selected (so as to remove columns instead of rows).

def main():
    pandasBasics()

if __name__ == "__main__":
    main()