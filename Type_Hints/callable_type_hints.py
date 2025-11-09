'''
In Python, everything that can be called (by placing parentheses after its name)
is a callable. Functions, lambdas and even classes are callable.
'''

from typing import Union, Callable

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b

def mult(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a * b

# The example below takes two numbers (either an int or a float), and a function that takes those two and returns also an int or a float.
def printBinaryMathOp(a: Union[int, float], b: Union[int, float], fn: Callable[ [Union[int, float], Union[int, float]], Union[int, float]]) -> None:
    print(f"{fn.__name__}({a}, {b}) = {fn(a, b)}")

def main():
    printBinaryMathOp(4, 5, add)
    printBinaryMathOp(4, 5, mult)

if __name__ == "__main__":
    main()