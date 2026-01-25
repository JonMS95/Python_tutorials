'''
This chapter is about extracting exactly the data you want from a DataFrame. We'll go slow
and layered, since it's one of the most used Pandas skills. This will work as a brush up for
other lessons.
'''

from handle_csv import readCSVFromPath, nl
import pandas as pd
from pandas.core.groupby.generic import DataFrameGroupBy

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
    
def sortingAndReindexing(df: pd.DataFrame) -> None:
    # Pretty friendly syntax. Use "by" input parameter as sorting criterion alongside ".sort_values()" method.
    # It can also be sorted by the index (.sort_index()) but it's not too common.
    df_sorted_by_country: pd.DataFrame = df.sort_values(by = "Country")
    print(f"df_sorted_by_country[['Customer Id', 'Country']].head():{nl}{df_sorted_by_country[['Customer Id', 'Country']].head()}")

    # Use "ascending" input parameter to tell whether resulting DataFrame should be ordered in ascending or descending order.
    df_sorted_by_country_inv: pd.DataFrame = df.sort_values(by = "Country", ascending = False)[['Customer Id', 'Country']]
    print(f"df_sorted_by_country_inv.head():{nl}{df_sorted_by_country_inv.head()}")

    # Same as in SQL, multiple columns can be used to order the resulting DataFrame. Provide a list of columns and a bool array to tell asc/desc for each column.
    df_sorted_by_customer_id_and_country: pd.DataFrame = df.sort_values(by = ["Customer Id", "Country"], ascending = [False, True])[["Customer Id", "Email"]]
    # DataFrame above is equivalent to: SELECT "Customer Id", "Email" FROM df ORDER BY "Customer Id" DESC, "Country" ASC;

    # DataFrames can be sorted in-place (every sorting performed up to now within the current file has led to a generated new DataFrame).
    # This can lead DataFrame's index to get messy afterwards, since the order in which every row is placed may be different after sorting.
    sort_in_place: pd.DataFrame = df
    print(f"sort_in_place.index before sorting:{nl}{sort_in_place.index}")

    # No need to return a DataFrame since sorting is being done over the DataFrame itself.
    sort_in_place.sort_values("Country", inplace = True)
    print(f"sort_in_place.head():{nl}{sort_in_place.head()}")
    print(f"sort_in_place.index after sorting:{nl}{sort_in_place.index}")
    
    # Reset the index in-place so as to preserve the changes in the target DataFrame (we will almost always want to do it this way).
    sort_in_place.reset_index(inplace = True)
    print(f"sort_in_place.index after resetting:{nl}{sort_in_place.index}")

def groupingAndAggregation(df: pd.DataFrame) -> None:
    # Same as SQL's GROUP clause, Pandas does also provide its own .groupby() method.
    grouped_dataframe: DataFrameGroupBy = df.groupby("Country")

    # Note that the type of the variable above is npt a DataFrame, but a groupby object. It does not perform any operation yet.
    # .size() method returns a count of all the rows per group. Also, .count() returns a count by column, which is not usually what we want.
    # Note that when using .size(), which (as a reminder) is basically a single dimension labeled data set (whereas DataFrame has associates
    # more than just a single column with each label/index value).
    count_per_country: pd.Series = grouped_dataframe.size()

    # A name can be given to the series:
    count_per_country.name = "Customers per country"

    print(f"count_per_country.head():{nl}{count_per_country.head()}")

    # Other aggregation functions can be used (.min(), .max(), .mean(), .sum()...).
    min_subscrption_date_per_country: pd.Series = grouped_dataframe["Subscription Date"].min()
    min_subscrption_date_per_country.name = "Earliest subscription date per country"
    print(f"min_subscrption_date_per_country.head():{nl}{min_subscrption_date_per_country.head()}")

    # Same as in SQL, data can be grouped by multiple criteria. In this case, we will group by Country and City (a list has to be passed instead
    # of just a single value). This way, smaller groups can be created (as the grouping requirements are more specific).
    df_grouped_by_country_and_city: DataFrameGroupBy = df.groupby(["Country", "City"])
    people_per_country_and_city: pd.Series = df_grouped_by_country_and_city.size()
    people_per_country_and_city.name = "People per city and country"
    print(f"people_per_country_and_city.head():{nl}{people_per_country_and_city.head()}")

    # On top of being able to group by multiple criteria (again, same as SQL), Pandas is able to perform multiple aggregation functions over
    # grouped data. Since multiple functions are performed, many columns will exist in the resulting object, which will be a DataFrame instead
    # of a Pandas Series. When using .agg() function, resulting column name as well as input DataFrame's column name and aggregation function
    # must be provided. Note that the resulting DataFrame's index will be composed by more than a single column since multiple criteria (many
    # columns) have been used to group data.
    early_sus_date_and_cust_cnt_per_country_and_city: pd.DataFrame = df.groupby(["Country", "City"]).agg(
        customer_count = ("Customer Id", "count"),
        earliest_subscription = ("Subscription Date", "min")
    )
    print(f"early_sus_date_and_cust_cnt_per_country_and_city.head():{nl}{early_sus_date_and_cust_cnt_per_country_and_city.head()}")

def selectAndFilter() -> None:
    # Retrieve a Pandas DataFrame object from a CSV file.
    df: pd.DataFrame = readCSVFromPath()

    # basicSelection(df)
    # ilocUsage(df)
    # locUsage(df)
    # booleanFiltering(df)
    # sortingAndReindexing(df)
    groupingAndAggregation(df)

def main():
    selectAndFilter()

if __name__ == "__main__":
    main()