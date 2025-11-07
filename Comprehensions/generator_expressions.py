'''
Generator expressions are comprehensions that don't store data in memory.
Instea, they yield each element lazily. They can be consumed by other
built-in functions such as "next" or "sum".
'''

from print_and_call_fn import printAndCallFn

def getTenFirstSquares() -> list[int]:
    squared_1_to_100 = (n ** 2 for n in range(100))
    ret = []
    for i in range(10):
        ret.append(next(squared_1_to_100))
    return ret

def sumFirstTenSquares() -> list[int]:
    squared_1_to_100 = (n ** 2 for n in range(100))
    return sum(squared_1_to_100)

def callGenExpFns():
    printAndCallFn(getTenFirstSquares)
    printAndCallFn(sumFirstTenSquares)