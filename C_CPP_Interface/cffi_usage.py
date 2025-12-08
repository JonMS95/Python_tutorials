'''
CFFI (C Foreign Function Interface) is an alternative to ctypes. Altough it's not Python's "native"
format, it's better when complex structs or pointer manipulation is involved.

The following command may be required so as to install required package(s):
pip install cffi
'''

from cffi import FFI
from _cffi_backend import Lib as dyn_lib
from timing_decorator import timingDecorator as t_deco
from getSOPaths import getPrimeNumbersPath
from primes_in_range import displayPrimeNumbersWithPython

def importPrimeNumbersLibrary() -> dyn_lib:
    ffi = FFI()

    ffi.cdef(""" bool isPrime(const int n); """)
    ffi.cdef("""
             void printPrimeNumbersInRange(const int range_start, const int range_end);
             """)

    return ffi.dlopen(getPrimeNumbersPath())

def testPrimeNumbers(numbers: list[int], lib: dyn_lib) -> None:
    for n in numbers:
        print(f"Is {n} prime? {lib.isPrime(n)}")

@t_deco
def displayPrimeNumbersWithC(primes_lib: dyn_lib, start: int = 2, end: int = 100) -> None:
    primes_lib.printPrimeNumbersInRange(start, end)
    print()

'''
Structs and other data types can be defined in-place, without any need for third-party dynamic libraries.
'''
def makePointStruct() -> None:
    ffi = FFI()

    ffi.cdef("""
            typedef struct
            {
                int x;
                int y;
                int z;
            } POINT;
            """)

    p0 = ffi.new("POINT *")
    
    p0.x = 1
    p0.y = 2
    p0.z = 3

    p_arr = ffi.new("POINT[]", 3)
    
    for i in range(0, len(p_arr)):
        p_arr[i].x = (i + 1) * 1
        p_arr[i].y = (i + 1) * 2
        p_arr[i].z = (i + 1) * 3

    print_point = lambda pt_name, pt = "no_name": print(f"{pt_name} -> x: {pt.x}, y: {pt.y}, z: {pt.z}")

    print_point("p0", p0)
    
    idx = 0
    for p in p_arr:
        print_point("p_arr[" + str(idx) + ']', p)
        idx += 1

def main():
    makePointStruct()
    cffi_lib = importPrimeNumbersLibrary()
    testPrimeNumbers([4, 7, 10, 11], cffi_lib)
    displayPrimeNumbersWithC(cffi_lib, 2, 10000)
    displayPrimeNumbersWithPython(2, 10000)

if __name__ == "__main__":
    main()