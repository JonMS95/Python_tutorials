'''
A common syntax to import components from a module is the following:
from MODULE import COMPONENT as ALIAS

Stating input variable types is not even mandatory in python, but it can be done
with the following syntax:

var: var_type
'''

from math import pi as PI_VALUE

def calc_area(radius: float):
    return ( PI_VALUE * ( float(radius) ** 2 ) )

def main():
    radius = input("Radius: ")
    print(f"Radius: {radius}, area: {calc_area(float(radius)):.2f}")

if __name__ == "__main__":
    main()