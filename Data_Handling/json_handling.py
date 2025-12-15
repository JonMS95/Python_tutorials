'''
This file covers some built-in json module basic usage examples. It supports both:
·JSON->Python (deserialization, use json.dumps() / json.dump())
·Python->JSON (serialization, use json.loads() / json.load())
'''

import json
from typing import Union as uni, Optional as opt, Callable as cble
from pathlib import Path
from os import getcwd

# From Python data to JSON object.
def serializationExample(input_data: dict[str, any], path: opt[str] = None) -> str:
    if path != None:
        p = Path(path)

        if not p.parent.exists():
            raise FileNotFoundError
        
        with open(p, "w") as file:
            json.dump(input_data, file)  # dump writes to a file.

    return json.dumps(input_data)        # dumps (with final 's') simply returns a JSON as a string.

def deserializationExample(input: str, load_from_path: bool = False) -> dict[str, any]:
    if load_from_path:
        p = Path(input)

        if not p.exists():
            raise FileNotFoundError
        with open(p, 'r') as json_file_path:
            return json.load(json_file_path)
    
    return json.loads(input)

def tryExceptBlock(function_name: cble, *args: any) -> None:
    try:
        print(f"{function_name.__name__}{args} -> {function_name(*args)}")
    except FileNotFoundError as fnfe:
        print(f"Target file could not be found: {fnfe}")
    except Exception as e:
        print(f"Caught generic exception: {e}")

def main():
    res_json_path: str = f"{getcwd()}/output_dummy.json"
    test_data_0: dict[str, uni[str, int, float]] = {
        "First Name"    : "John",
        "Last Name"     : "Doe" ,
        "Age"           : 33    ,
        "Height"        : 1.80  ,
        "Weight"        : 78.9  ,
    }
    test_data_1: str = ''               \
    '{'                                 \
    '   "First name"    : "Jon",'       \
    '   "Last Name"     : "Jameson",'   \
    '   "Age"           : 29,'          \
    '   "Height"        : 1.65,'        \
    '   "Weight"        : 56.7'         \
    '}'

    tryExceptBlock(serializationExample, test_data_0, res_json_path)
    tryExceptBlock(serializationExample, test_data_1)
    tryExceptBlock(deserializationExample, res_json_path, True)
    tryExceptBlock(deserializationExample, test_data_1, False)

if __name__ == "__main__":
    main()
