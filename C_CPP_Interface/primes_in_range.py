from timing_decorator import timingDecorator as t_deco

def checkIfNumberIsPrime(n: int) -> bool:
    for i in range(2, n, 1):
        if n % i == 0:
            return False
    
    return True

@t_deco
def displayPrimeNumbersWithPython(start: int = 2, end: int = 100) -> None:
    for i in range(start, end + 1, 1):
        if checkIfNumberIsPrime(i):
            print(str(i) + ' ', end='')
    print()