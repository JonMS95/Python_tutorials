'''
Same as in Java, a data class refers to a class that only provides fields
and methods for accessing them (getters/setters). 

Data classes were introduced in Python 3.7 via @dataclass. They simplify
boilerplate code for classes by automaticalllly generating __init__,
__repr__, __eq__ and other methods, makeing them great for classes which
are only intended to be storing data.
'''

# Note that current file's name is data_classes so as to avoid naming collisions.
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
    z: int = 0  # Default values can be provided here too.

def main():
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    print(f"p1: {p1}")
    print(f"p1 == p2: {p1 == p2}")

if __name__ == "__main__":
    main()