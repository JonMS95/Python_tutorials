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

def basicBroadcastingSum(x: np.array = np.array([_ for _ in range(1, 5)]), y = 5) -> np.array:
    z = x + y
    print(f"{x} + {y} = {z}")
    return (x + y)

def main():
    basicBroadcastingSum()

if __name__ == "__main__":
    main()