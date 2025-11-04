from print_and_call_fn import printAndCallFn

def slowSquares(n: int = 5) -> list[int]:
    squares = []
    for i in range(n):
        squares.append(i ** 2)
    return squares

def squares(n: int = 5) -> list[int]:
    return [i**2 for i in range(n)]

def evenSquares(n: int = 10) -> list[int]:
    return [i ** 2 for i in range(n) if i % 2 == 0]

def numberLetterPairs(numbers: list[int] = [1, 2, 3], letters: list[str] = ['a', 'b']) -> list[list[int, str]]:
    return [(x, y) for x in numbers for y in letters]

def makeMatrix(rows: int = 3, cols: int = 3) -> list[list[int]]:
    return [[0 for b in range(cols)] for a in range(rows)]

def callListCompFns():
    printAndCallFn(slowSquares)
    printAndCallFn(squares)
    printAndCallFn(evenSquares)
    printAndCallFn(numberLetterPairs)
    printAndCallFn(makeMatrix)