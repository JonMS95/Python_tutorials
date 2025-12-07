'''
CTypes is the traditional way to import C-program symbols. See getCSymbols function
below to learn how to use it properly.
'''

from pathlib import Path as path
import ctypes
from timing_decorator import timingDecorator as t_deco
from primes_in_range import displayPrimeNumbersWithPython

def getCSymbols() -> ctypes.CDLL:
    lib_path = path(__file__).parent / "c_lib" / "lib" / "prime_numbers.so"
    
    if not lib_path.exists():
        raise FileNotFoundError(f"{lib_path} does not exist!")
    
    # Convert Path to string and create ctypes.CDDL type object.
    lib = ctypes.CDLL(str(lib_path.resolve()))
    
    # isPrime: int isPrime(int n)
    lib.isPrime.argtypes = [ctypes.c_int]   # Specify input parameter's types.
    lib.isPrime.restype  = ctypes.c_bool    # Specify return type.

    # printPrimeNumbersInRange: void printPrimeNumbersInRange(int start, int end)
    lib.printPrimeNumbersInRange.argtypes = [ctypes.c_int, ctypes.c_int]
    lib.printPrimeNumbersInRange.restype  = None

    return lib

def testPrimeNumbers(numbers: list[int], lib: ctypes.CDLL) -> None:
    for n in numbers:
        print(f"Is {n} prime? {lib.isPrime(n)}")

@t_deco
def displayPrimeNumbersWithC(primes_lib: ctypes.CDLL, start: int = 2, end: int = 100) -> None:
    primes_lib.printPrimeNumbersInRange(start, end)
    print()

def main():
    c_lib = getCSymbols()
    testPrimeNumbers([4, 7, 10, 11], c_lib)
    displayPrimeNumbersWithC(c_lib, 2, 10000)
    displayPrimeNumbersWithPython(2, 10000)

if __name__ == "__main__":
    main()