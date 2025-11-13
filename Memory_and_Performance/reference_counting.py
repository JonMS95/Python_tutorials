'''
In CPython (default Pythin implementation), memory management is based in reference counting
(same as smart pointer in C++). Each object keeps track of how many references there are to it.

When the count drops to zero, Python automatically frees the memory previously allocated for it.
'''

import sys

def main():
    a: int = 3
    b: int = a # b is a reference to a

    print(sys.getrefcount(a))

    print(f"sys.getrefcount(a): {sys.getrefcount(a)} (before)")
    del b # references number will be decremented
    print(f"sys.getrefcount(a): {sys.getrefcount(a)} (after)")

    # The same logic goes for data collections (lists, tuples...)

    c: list[int] = [1, 2, 3]
    d: list[int] = c

    print(f"sys.getrefcount(a): {sys.getrefcount(c)} (before)")
    del d
    print(f"sys.getrefcount(a): {sys.getrefcount(c)} (after)")

if __name__ == "__main__":
    main()