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

    p:Path = Path(file_path)
    
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

def writeToCSV(csv_file_path: str, input_data: csv_data_ret_type) -> None:
    if not len(input_data):
        raise ValueError("No input data was provided")
    
    p:Path = Path(csv_file_path)

    if not len(csv_file_path) or not p.parent.exists():
        raise(ValueError(f"Path does not exist: {csv_file_path}"))

    csv_write_fn: cble = None

    if type(input_data[0]) == dict:
        csv_write_fn = csv.DictWriter
    elif type(input_data[0]) == list:
        csv_write_fn = csv.writer
    else:
        raise TypeError(f"Input data type should be either list or dict but {type(input_data[0])} was provided")

    with open(csv_file_path, 'w', newline="") as csv_file:
        writer: cble = None
        if type(input_data[0]) == dict:
            print(input_data[0].keys())
            writer = csv.DictWriter(csv_file, fieldnames=list(input_data[0].keys()))
            writer.writeheader()
        else:
            writer = csv_write_fn(csv_file)
        writer.writerows(input_data)

def main():
    csv_file_path: str = getcwd() + '/' + "data.csv"
    retrieved_types_tuple: types_as_tuple = (str, int, float)
    retrieved_types_dict: types_as_dict = {"name" : str, "age" : int, "height" : float}

    tryReadFromCSV(retrieveDataFromCSV, csv_file_path, retrieved_types_tuple, False)
    tryReadFromCSV(retrieveDataFromCSV, csv_file_path, retrieved_types_dict)

    output_csv_data_path_0: str = getcwd() + '/' + "dummy_output_0.csv"
    output_csv_data_path_1: str = getcwd() + '/' + "dummy_output_1.csv"

    output_list: list[any] = [
        ["name", "age", "height"],
        ["John", 19, 1.70       ],
        ["Jessica", 35, 1.63    ],
        ["Lisa", 25, 1.69       ],
    ]

    output_dict: list[str, any] = [
        {"name": "Jason", "age": 17, "height": 1.68},
        {"name": "Gina", "age": 21, "height": 1.59},
        {"name": "Paul", "age": 47, "height": 1.89},
    ]

    writeToCSV(output_csv_data_path_0, output_list)
    writeToCSV(output_csv_data_path_1, output_dict)

if __name__ == "__main__":
    main()