'''
Vectorization is like broadcasting in spirit (apply one operation to many elements), but without
NumPy needing to adjust shapes.

Broadcasting is more about making shapes compatible. Vectorization, instead, is rather about
executing the target operation efficiently once the shapes are compatible. It usually involves
replacing pure Python operations by C-code ones, which are way more optimized and leave Python
itself out of the picture. In fact, the aim is to call Python interpreter just once.

By default, basic math operators (+, -, *, /) are performed element-wise in NumPy.

On top of the features mentioned above, NumPy provides reductions. These reduction operations are
procedures that act over the wholeness or part of an array and return a scalar. Note that an axis
should be specified (columns (0), rows(1)...). Mental-model: axis is the dimension that
disappears.
'''

import numpy as np
from performance_timer import timingDecorator
from math import sqrt
from random import randint as ri

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
    
    print(f"(np.array_equal(loopAddition(x, k) == vectorizedAddition(x, k))): ", (np.array_equal(loopAddition(x, k), vectorizedAddition(x, k))))
    # Note that "==" operator is not used in this case since its result is another array (full of Bool's): "==" leads to an element-wise comparison.

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

    print(f"(np.array_equal(loopSqrt(x), vectorizedSqrt(x))): ", (np.array_equal(loopSqrt(x), vectorizedSqrt(x))))

@timingDecorator
def vectorizedMatrixAddition(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    return A + B

@timingDecorator
def vectorizedMatrixMultiplication(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    return A * B
# Note that different from when using matmul or "@" op, "*" operator performs multiplication element-wise.
# Same goes for every other basic operator (+, -, * and / are all performed "per element").

def testVectorizedMatrixOperation() -> None:
    A: np.ndarray = np.array([[ri(0, 10) for col in range(3)] for row in range(4)])
    B: np.ndarray = np.array([[ri(0, 10) for col in range(3)] for row in range(4)])

    print(f"A:\n{A}\n\nB:\n{B}")

    C: np.ndarray = vectorizedMatrixAddition(A, B)
    D: np.ndarray = vectorizedMatrixMultiplication(A, B)

    print(f"C (= A + B):\n{C}\n\nD (= A * B):\n{D}\n")

def getMatrixSum(A: np.ndarray, op_axis: int = 0) -> float:
    return np.sum(A, dtype = float, axis = op_axis)

def getMatrixDimMean(A: np.ndarray, op_axis: int = 0) -> float:
    return np.mean(A, dtype = float, axis = op_axis)

def testReductions() -> None:
    A: np.ndarray = np.array([[ri(0, 10) for col in range(3)] for row in range(10)])

    print(f"A:\n{A}\n\n")

    B: np.ndarray = getMatrixSum(A)
    C: np.ndarray = getMatrixDimMean(A)

    print(f"B (column-wise sum):\n{B}\n\n")
    print(f"C (column-wise mean):\n{C}\n\n")

def main():
    testAddition()
    testSquareRoot()
    testVectorizedMatrixOperation()
    testReductions()

if __name__ == "__main__":
    main()