'''
Broadcasting is a powerful NumPy feature that pretends different sized arrays
or elements to have the same size so as to make some operations more efficient.
For instance, having:
x = np.array([1, 2, 3, 4])
y = 5

There's no way y can be added to x. However, there's a mechanism namely NumPy
that can shorten the path to perform the application so taht there's no need
to generate an array of 5's explictly then add it to the NumPy array. 
'''

import numpy as np

def basicBroadcastingSum(x: np.ndarray = np.array([_ for _ in range(1, 5)]), y = 5) -> np.array:
    z = x + y
    print(f"{x} + {y} = {z}")
    return (x + y)

def scalarToVector() -> np.ndarray:
    x: np.ndarray = np.arange(10, 50, 10)
    y: int = 5
    z: np.ndarray = x + y

    print(f"Scalar to vector broadcasting: {x} + {y} = {z}")
    return z

def vectorToMatrix() -> np.ndarray:
    X: np.ndarray = np.arange(1, 7).reshape(2, 3)   # Creates a 1-D vector of numbers from 1 to 6 (inclusive), then it rearranges numbers into a 2 x 3 matrix.
    y: np.ndarray = np.array([10, 20, 30])          # Creates a 1-D vector with given elements.
    C: np.ndarray = X + y

    print(f"Vector to matrix broadcasting:\r\nX: {X}\r\ny: {y}\r\nC: {C}")
    return C

def main():
    basicBroadcastingSum()
    scalarToVector()
    vectorToMatrix()

if __name__ == "__main__":
    main()