'''
Python uses LEGB rule for resolving names:

·L: local (inside current function)
·E: enclosing (any outer function scopes)
·G: global (module-level)
·B: built-in (Python's reserved names like len, sum, ...)
'''

from math import pi as MATH_PI_VALUE

x = 10 # Global

# MATH_PI_VALUE: built-in

def outer():
    x = 20 # Enclosing
    
    def inner(): # Nested functions can be defined in Python.
        x = 30
        print(f"x into {inner.__name__} function: {x}")
    
    inner()
    print(f"x into {outer.__name__} function: {x}")

def main():
    outer()

if __name__ == "__main__":
    main()