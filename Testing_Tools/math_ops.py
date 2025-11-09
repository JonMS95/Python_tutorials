'''
This file will simply host some dummy functions to be used later by fllow testing modules.
'''

from typing import Union

num_type = Union[int, float]

def sub(a: num_type, b: num_type) -> num_type:
    return (a - b)

def div(a: num_type, b: num_type) -> num_type:
    return a / b    # Raises ZeroDivisionError by itself if necessary. 
