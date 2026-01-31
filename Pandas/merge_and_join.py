'''
This file will include some examples covering Pandas .merge() method (equivalent to SQL's JOIN).
Different from other files in this Pandas chapter, DataFrames will be fully custom instead of
being imported from CSV files so as to make them more understandable.

Examples below will refer to merge use cases as in SQL: INNER JOIN, LEFT/RIGHT JOIN, FULL OUTER JOIN.
'''

import pandas as pd
from handle_csv import nl

df_cusomters: pd.DataFrame = pd.DataFrame({
    "Customer ID"   :   [0, 1, 2, 3]                        ,
    "Name"          :   ["Alice", "Bob", "Charlie", "Daisy"],
})

df_subscriptions: pd.DataFrame = pd.DataFrame({
    "Customer ID"   :   [1, 3]              ,
    "Plan"          :   ["Premium", "Basic"],
})

# Equivalent to INNER JOIN, will keep only matching rows in both DataFrames.
def mergeDataFrames(df_left: pd.DataFrame, df_right: pd.DataFrame, method: str = "inner") -> pd.DataFrame:
    if method not in ["inner", "left", "right", "outer"]:
        raise ValueError(f"Provided method ({method}) does not exist")
    
    merged: pd.DataFrame =  pd.merge(   left  = df_left       ,
                                        right = df_right      ,
                                        on    = "Customer ID" ,
                                        how   = method
                                        )
    return merged

# Aside .merge(), there is a method in Pandas known as .join(). Instead of the joining based on a column name, it will use the index as matching criterion by default.
def joinDataFrames(df_left: pd.DataFrame, df_right: pd.DataFrame, method: str = "inner", index: str = "Customer ID") -> pd.DataFrame:
    if method not in ["inner", "left", "right", "outer"]:
        raise ValueError(f"Provided method ({method}) does not exist")
    
    if index not in df_left.columns or index not in df_right.columns:
        raise ValueError(f"Provided index ({index}) does not exist in some of the given DataFrames")

    df_left_index:  pd.DataFrame = df_left.set_index(index)
    df_right_index: pd.DataFrame = df_right.set_index(index)

    df_joint: pd.DataFrame = df_left_index.join(df_right_index, how = method)

    return df_joint

def main():
    print(f"(Merge) Inner Join(df_cusomters, df_subscriptions):{nl}{mergeDataFrames(df_cusomters, df_subscriptions)}")          # Only rows matching "on" condition will be saved.
    print(f"(Merge) Left  Join(df_cusomters, df_subscriptions):{nl}{mergeDataFrames(df_cusomters, df_subscriptions, 'left')}")  # All rows from left DataFrame will be kept.
    print(f"(Merge) Right Join(df_cusomters, df_subscriptions):{nl}{mergeDataFrames(df_cusomters, df_subscriptions, 'right')}") # Same as the example above but with the right DataFrame.
    print(f"(Merge) Outer Join(df_cusomters, df_subscriptions):{nl}{mergeDataFrames(df_cusomters, df_subscriptions, 'outer')}") # Data from both DataFrames will be stored in the resulting DF by placing NaN on the missing column values.

    print(f"(Merge) Inner Join(df_cusomters, df_subscriptions):{nl}{joinDataFrames(df_cusomters, df_subscriptions)}")
    print(f"(Merge) Left  Join(df_cusomters, df_subscriptions):{nl}{joinDataFrames(df_cusomters, df_subscriptions, 'left')}") 
    print(f"(Merge) Right Join(df_cusomters, df_subscriptions):{nl}{joinDataFrames(df_cusomters, df_subscriptions, 'right')}")
    print(f"(Merge) Outer Join(df_cusomters, df_subscriptions):{nl}{joinDataFrames(df_cusomters, df_subscriptions, 'outer')}")

if __name__ == "__main__":
    main()