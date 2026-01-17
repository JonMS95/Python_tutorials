'''
This file will show some examples so as to understand Pandas basics.
'''

import pandas as pd
import numpy as np

endl: str = "\r\n\r\n"

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

def main():
    pandasBasics()

if __name__ == "__main__":
    main()