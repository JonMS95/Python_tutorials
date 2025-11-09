'''
Python provides a wide set of special methods that can be defined
for every user-made class providing various functionalities. Take
a look at the examples so as to grasp all the nuances about them.

Note: over 50 special class methods exist in python, we will
constrain t some of the most popular below.
'''

class Point:
    # Class constructor
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y
    
    # Determines what should be printed when calling print(obj), used either when calling print or casting as str
    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

    # Meant to be the "official version" of what the method above retrieves (target: developers)
    def __repr__(self):
        return f"{self.x} {self.y}"

    # Specifies how addition operation should be performed for two objects of the current class
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Tells how should "==" operator be used
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

def main():
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    print(p1)
    print(repr(p2))
    p3 = p1 + p2
    print(f"{repr(p1)} + {repr(p2)} = {repr(p3)}")
    print(f"p1 == p2 -> {p1 == p2}")

if __name__ == "__main__":
    main()