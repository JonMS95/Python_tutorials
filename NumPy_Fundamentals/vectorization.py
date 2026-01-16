'''
Vectorization is like broadcasting in spirit (apply one operation to many elements), but without
NumPy needing to adjust shapes.

Broadcasting is more about making shapes compatible. Vectorization, instead, is rather about
executing the target operation efficiently once the shapes are compatible. It usually involves
replacing pure Python operations by C-code ones, which are way more optimized and leave Python
itself out of the picture. In fact, the aim is to call Python interpreter just once.
'''

import numpy as np
from performance_timer import timingDecorator
from math import sqrt

@timingDecorator
def loopAddition(x: np.ndarray, scalar: float) -> np.ndarray:
    y = np.empty_like(x, dtype = float) # Creates a NumPy array with the same dimensions as the input (x) but composed by floating point numbers.
    
    for i in range(len(x)):
        y[i] = x[i] + scalar
    
    return y

@timingDecorator
def vectorizedAddition(A: np.ndarray, b: int):
    C: np.ndarray = A + b
    return C

def testAddition() -> None:
    x_size = 10 ** 5
    
    x: np.ndarray = np.array([_ for _ in range(x_size)])
    k: float = 3.3
    
    # print(f"(loopAddition) {x} + {k} = {loopAddition(x, k)}")
    
    print(f"loopAddition(x, k) == vectorizedAddition(x, k):", (loopAddition(x, k) == vectorizedAddition(x, k)))

@timingDecorator
def loopSqrt(x: np.ndarray) -> np.ndarray:
    y = np.empty_like(x, dtype = float)

    for i in range(len(x)):
        y[i] = 0.0 if x[i] <= 0 else sqrt(x[i])
    
    return y

@timingDecorator
def vectorizedSqrt(A: np.ndarray) -> np.ndarray:
    B: np.ndarray = np.zeros_like(A, dtype = float) # Same as empty_like, but setting every element equal to zero by default.

    mask: np.ndarray = A > 0    # Creates a bool mask where each element equals True solely for those meeting specified condition.
    
    B[mask] = np.sqrt(A[mask])

    return B

def testSquareRoot() -> None:
    x_size = 10 ** 5
    x: np.ndarray = np.array([_ ** 2 for _ in range(x_size)])

    print(f"loopSqrt(x) == vectorizedSqrt(x):", (loopSqrt(x) == vectorizedSqrt(x)))

def main():
    testAddition()
    testSquareRoot()

if __name__ == "__main__":
    main()