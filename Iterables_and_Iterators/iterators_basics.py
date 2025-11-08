'''
In Python, an iterable is a data structure with various elements that can be iterated.
The elements that are used to iterate over those structures are called iterators.

Iterables can be created by using "iter" keyword
'''

def iteratorsDemo() -> None:
    nums = [10, 20, 30]
    it = iter(nums) # Create an iterator for an iterable object.
    # Use "next" to get the next element as iterable. 
    print(next(it)) # 10
    print(next(it)) # 20
    print(next(it)) # 30
    # next(it) # Wuod raise an exception when called since no other element exists.

def printNums(nums: list[int] = [4, 1, 6, 2, 8, 3]) -> None:
    it = iter(nums)
    while True:
        try:
            value = next(it)
            print(value)
        except StopIteration:
            break

def main():
    print(f"iteratorsDemo(): {iteratorsDemo()}")
    print("printNums(): ", end = "")
    printNums()

if __name__ == "__main__":
    main()