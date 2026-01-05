'''
NumPy's memory model is powerful but there are some subtle nuances that may
be hard to grasp:
·Arrays are memory blocks: every ndarray stores data in a contiguous block
of memory.
·NumPy keeps track of how to interpret each block via dshape (dimensions)
and strides (how many bytes to jump to get the next element).
This is what makes NumPy so fast. thus, NumPy arrays are not Python lists,
but homogeneous memory buffers with metadata.
'''

import numpy as np

'''
NumPy views do not behave same as SQL or C++ views (nor as generator
expressions in Python). Instead, memory blocks are created when
instantiated but they point at already existing memory blocks. Therefore,
they should be handled with care as modifying the view implies changing the
content of the pointed memory blocks.
'''
def viewsinNumPy() -> None:
    x = np.array([_**2 for _ in range(10)])
    x_view = x[1:9]

    print("x: ", x)
    print("x_view: ", x_view)
    
    x_view[0] = 100
    
    print("After modifying view (x_view[0] = 100), x: ", x)

'''
Copies create completely new arrays, stored in new memory blocks. Thus,
modifying the copy leaves the original array unmodified.
'''
def copiesInNumpy(input: np.array) -> None:
    x = input.copy()
    y = input[0:(input.size - 1)].copy()
    
    x[0] = 1
    y[-1] = 777

    print(f"x: {x}")
    print(f"y: {y}")
    print(f"input: {input}")

def checkSharedMemory(x: np.array, y: np.array) -> None:
    sh_mem: bool = np.shares_memory(x, y)
    print(f"Do x {x} and y {y} share memory? {'Yes' if sh_mem else 'No'}")
    
def testSharedMemory() -> None:
    a = np.array([_ * 10 for _ in range(10)])
    b = a.copy()
    checkSharedMemory(a, b)
    c = a[1:3]
    checkSharedMemory(a, c)

def main():
    viewsinNumPy()
    copiesInNumpy(np.array([_ * 2 for _ in range(10)]))
    testSharedMemory()

if __name__ == "__main__":
    main()