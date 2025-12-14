'''
This file covers some built-in json module basic usage examples. It supports both:
·JSON->Python (deserialization, use json.dumps() / json.dump())
·Python->JSON (serialization, use json.loads() / json.load())
'''

import json
from typing import Union as uni, Optional as opt
from pathlib import Path
from os import getcwd

# From Python data to JSON object.
def serializationExample(path: opt[str] = None) -> str:
    test_data: dict[str, uni[str, int, float]] = {
        "First Name"    : "John",
        "Last Name"     : "Doe" ,
        "Age"           : 33    ,
        "Height"        : 1.80  ,
        "Weight"        : 78.9  ,
    }

    if path != None:
        p = Path(path)

        if not p.parent.exists():
            raise FileNotFoundError
        
        with open(p, "w") as file:
            json.dump(test_data, file)  # dump writes to a file.

    return json.dumps(test_data)        # dumps (with final 's') simply returns a JSON as a string.

def main():
    res_json_path: str = f"{getcwd()}/output_dummy.json"
    
    try:
        print(f"serializationExample({res_json_path}): {serializationExample(res_json_path)}")
    except FileNotFoundError as fnfe:
        print("File could not be found: {fnfe}")
    except Exception as e:
        print("Caught generic exception: {e}")


if __name__ == "__main__":
    main()