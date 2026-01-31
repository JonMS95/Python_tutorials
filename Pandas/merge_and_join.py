'''
This file will include some examples covering Pandas .merge() method (equivalent to SQL's JOIN).
Different from other files in this Pandas chapter, DataFrames will be fully custom instead of
being imported from CSV files so as to make them more understandable.
'''

import pandas as pd

df_cusomters: pd.DataFrame = pd.DataFrame({
    "Customer ID"   :   [0, 1, 2, 3]                        ,
    "Name"          :   ["Alice", "Bob", "Charlie", "Daisy"],
})

df_subscriptions: pd.DataFrame = pd.DataFrame({
    "Customer ID"   :   [1, 3]              ,
    "Plan"          :   ["Premium", "Basic"],
})

def main():
    pass

if __name__ == "__main__":
    main()