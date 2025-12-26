'''
This file covers some basic csv file handling in Python. 
'''

import csv
from os import getcwd
from pathlib import Path
from typing import Optional as opt, Union as uni, Callable as cble

csv_raw_data_mat_type = list[list[str]]
csv_raw_data_dicts_type = list[dict[str, str]]
csv_raw_data_ret_type = uni[csv_raw_data_mat_type, csv_raw_data_dicts_type]

csv_data_mat_type = list[list[any]]
csv_data_dicts_type = list[dict[str, any]]
csv_data_ret_type = uni[csv_data_mat_type, csv_data_dicts_type]

types_as_tuple = tuple[type]
types_as_dict = dict[str, type]


def retrieveRawDataFromCSV(file_path: str, return_as_dict: bool = True) -> csv_data_ret_type:
    if file_path == None or file_path == "":
        raise ValueError("Invalid path provided")

    p = Path(file_path)
    
    if not p.exists():
        raise FileNotFoundError(f"File in provided path {file_path} could not be found")

    data_line: bool = False
    ret: uni[list[list[str]], list[dict[str, str]]] = []

    with open(file_path) as csv_file:
        csv_read_fn: callable
        if return_as_dict:
            csv_read_fn = csv.DictReader
        else:
            csv_read_fn = csv.reader
        for row in csv_read_fn(csv_file):
            ret.append(row)
    
    return ret

def retrieveDataFromCSV(file_path: str, types: uni[types_as_tuple, types_as_dict], return_as_dict: bool = True) -> uni[csv_data_ret_type, None]:
    ret: csv_data_ret_type = retrieveRawDataFromCSV(file_path, return_as_dict)

    if not len(ret):
        return None

    if not return_as_dict:
        for r_idx in range(1, len(ret)):
            row = ret[r_idx]
            if len(types) != len(row):
                raise ValueError(f"Types tuple and row size do not match ({len(types)} != {len(row)})")
            for i in range(1, len(types)):
                row[i] = types[i](row[i])
    else:
        for row in ret:
            for k in types.keys():
                if k not in row.keys():
                    raise KeyError(f"Key {k} not found in data set")
                row[k] = types[k](row[k])
    
    return ret

def tryReadFromCSV(function_name: cble, *args: any) -> None:
    try:
        csv_data = retrieveDataFromCSV(*args)
    except ValueError as ve:
        print(f"ValueError exception caught: {ve}")
    except FileNotFoundError as fnfe:
        print(f"FileNotFoundError exception caught: {fnfe}")
    except Exception as e:
        print(f"Generic exception caught: {e}")
    else:
        print(f"{function_name.__name__}{args} -> {function_name(*args)}")
        if len(csv_data) > 1:
            for row in csv_data:
                print(row)

def main():
    csv_file_name: str = "data.csv"
    csv_file_path: str = getcwd() + '/' + csv_file_name
    retrieved_types_tuple: types_as_tuple = (str, int, float)
    retrieved_types_dict: types_as_dict = {"name" : str, "age" : int, "height" : float}

    tryReadFromCSV(retrieveDataFromCSV, csv_file_path, retrieved_types_tuple, False)
    tryReadFromCSV(retrieveDataFromCSV, csv_file_path, retrieved_types_dict)

if __name__ == "__main__":
    main()