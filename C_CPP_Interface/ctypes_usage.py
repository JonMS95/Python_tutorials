'''
CTypes is the traditional way to import C-program symbols.
'''

from pathlib import Path as path
from time import time as getCurTime
import ctypes

def timingDecorator(target_fn):
    def wrapper(*args, **kwargs):
        start_time = getCurTime()
        ret = target_fn(*args, **kwargs)
        end_time = getCurTime()
        
        print(f"{target_fn.__name__} functions\'s execution took {(end_time - start_time):.2f} seconds")
        
        return ret
    return wrapper

def getCSymbols() -> ctypes.CDLL:
    lib_path = path(__file__).parent / "prime_numbers.so"
    
    if not lib_path.exists():
        raise FileNotFoundError(f"{lib_path} does not exist!")
    
    # Convert Path to string
    lib = ctypes.CDLL(str(lib_path.resolve()))
    
    # isPrime: int isPrime(int n)
    lib.isPrime.argtypes = [ctypes.c_int]
    lib.isPrime.restype  = ctypes.c_bool

    # printPrimeNumbersInRange: void printPrimeNumbersInRange(int start, int end)
    lib.printPrimeNumbersInRange.argtypes = [ctypes.c_int, ctypes.c_int]
    lib.printPrimeNumbersInRange.restype  = None

    return lib

def testPrimeNumbers(numbers: list[int], lib: ctypes.CDLL) -> None:
    for n in numbers:
        print(f"Is {n} prime? {lib.isPrime(n)}")

@timingDecorator
def displayPrimeNumbersWithC(primes_lib: ctypes.CDLL, start: int = 2, end: int = 100) -> None:
    primes_lib.printPrimeNumbersInRange(start, end)
    print()

def checkIfNumberIsPrime(n: int) -> bool:
    for i in range(2, n, 1):
        if n % i == 0:
            return False
    
    return True

@timingDecorator
def displayPrimeNumbersWithPython(start: int = 2, end: int = 100) -> None:
    for i in range(start, end + 1, 1):
        if checkIfNumberIsPrime(i):
            print(str(i) + ' ', end='')
    print()

def main():
    c_lib = getCSymbols()
    testPrimeNumbers([4, 7, 10, 11], c_lib)
    displayPrimeNumbersWithC(c_lib, 2, 10000)
    displayPrimeNumbersWithPython(2, 10000)

if __name__ == "__main__":
    main()