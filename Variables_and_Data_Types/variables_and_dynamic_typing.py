'''
In Python, variable typing is dynamic, so variable types are determined during runtime.
Variable types can be displayed with "type" built-in function.

Basic types in Python are int, float, bool, str and NoneType. The latter is a special type
used to represent absence of any value, similar to NULL/nullptr in C/C++.
'''

from math import pi

def printVariableAndType(input_var):
    print(f"input_var: {input_var}, type: {type(input_var)}")

def main():
    a = 3
    b = "Three"
    printVariableAndType(a)
    printVariableAndType(pi)
    printVariableAndType(b)
    printVariableAndType(True)
    printVariableAndType(None)

if __name__ == "__main__":
    main()