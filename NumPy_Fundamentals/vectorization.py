'''
Vectorization is like broadcasting in spirit (apply one operation to many elements), but without
NumPy needing to adjust shapes.

Broadcasting is more about making shapes compatible. Vectorization, instead, is rather about
executing the target operation efficiently once the shapes are compatible. It usually involves
replacing pure Python operations by C-code ones, which are way more optimized and leave Python
itself out of the picture. In fact, the aim is to call Python interpreter just once.
'''

import numpy as np



def main():
    pass

if __name__ == "__main__":
    main()