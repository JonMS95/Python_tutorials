'''
A nested or inner function is a function that's known within
a function's scope. It can access variables from out its scope
even after outer function has finished running.

Apart from well-known variable types, functions can be returned
as well (even those defined within a function).
'''

def outer(x: int = 10) -> None:
    x += 1
    def inner() -> None:
        print(f"x: {x}")
    inner()

def powerMaker(exponent: int = 2):
    def power(base: int) -> int:
        return base ** exponent
    return power

# Note that a variable can even be a function in Python.
get_square = powerMaker(2)
# get_square is now equivalent to a function taht could have been defined as follows:
# def getSquare(base: int) -> int:
#     return base ** 2

get_cube = powerMaker(3)
# In a similar fashion, get_cube would be similar to:
# def getCube(base: int) -> int:
#     retrun base ** 3

def main():
    outer()
    print(f"get_square(10): {get_square(10)}")
    print(f"get_cube(9): {get_cube(9)}")


if __name__ == "__main__":
    main()