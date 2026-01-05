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

def main():
    viewsinNumPy()

if __name__ == "__main__":
    main()