'''
Different from generating iterable objects, creating a generator expressions
consumes little memory. When using generator expressions, elements are generated
lazily (on demand). This way, an element is generated each time "next" keyword
is called.

Recommended usage:
·list: when items are meant to be accessed multiple times.
·generator expression: when iterating is only needed once and memory is a concern.
'''

import sys

def listVSGenMemUsage(n: int = (10 ** 6)) -> None:
    n_list  = [x for x in range(n)]
    n_gen   = (x for x in range(n))
    print(f"List size: {sys.getsizeof(n_list)}")
    print(f"Generator size: {sys.getsizeof(n_gen)}")

def main():
    print(f"listVSGenMemUsage(): {listVSGenMemUsage()}")

if __name__ == "__main__":
    main()