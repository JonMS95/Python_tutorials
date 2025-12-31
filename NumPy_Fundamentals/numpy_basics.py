'''
NumPy (Numerical Python) is a fundamental Python library for scientific computing,
often used in data science, math and engineering tasks. It offers efficient,
high-performance array manipulation, mathematical functions and so on.
'''

import numpy as np # NumPy is commonly imported as "np". Not mandatory but almost a de-facto standard.

def numpyBasicUsage() -> None:
    np_elements: list[any] = []
    
    np_elements.append(np.array([1, 2, 3]))     # Simple 1-D array of integers.
    np_elements.append(np.zeros((3, 4)))        # 3 x 4 matrix (2-D array) full of zeros.
    np_elements.append(np.ones((2, 3, 4)))      # 2 x 3 x 4 tensor (3-D array) full of ones.
    np_elements.append(np.arange(0, 10, 2))     # Sequence of numbers from 0 to 8 with step 2.
    np_elements.append(np.linspace(0, 1, 5))    # 5 numbers evenly spaced between 0 and 1 inclusive.

    for np_elem in np_elements:
        print(np_elem)
        print(np_elem.shape)    # Array dimensions.
        print(np_elem.ndim)     # Rank / number of axes.
        print(np_elem.dtype)    # Data type.
        print(np_elem.size)     # Total elements
        print()

def main():
    numpyBasicUsage()

if __name__ == "__main__":
    main()
