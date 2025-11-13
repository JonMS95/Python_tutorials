'''
"timeit" is a built-in library which makes simple measuring short code snippet's execution time.
Use "timeit" method by providing the code between quotes or fucntion's name. 
'''

import timeit

def main():
    setup = "nums = list(range(1000))"
    print("Loop:", timeit.timeit("total = 0\nfor n in nums: total += n", setup=setup, number=10000))
    print("Comprehension:", timeit.timeit("sum([n for n in nums])", setup=setup, number=10000))
    print("Built-in sum:", timeit.timeit("sum(nums)", setup=setup, number=10000))


if __name__ == "__main__":
    main()