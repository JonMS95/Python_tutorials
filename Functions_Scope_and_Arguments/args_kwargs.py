'''
Python allows handling a variable number of input parameters flexibly.

·args: tuple of unnamed arguments.
·kwargs: dict of named arguments.

When it comes to retrieving arguments as args, * operator is used. In this context,
using * stands for: take all the positional arguments passed to this function and
pack them into a single tuple called args. When calling a function, *args is equal
to unpacking the elements while solely using args does unpack nothing. By the way,
calling it explicitly "*args" is not mandatory, but placing an asterisk preceeding
the variable name is.

On the other hand, **kwargs is used to pack all of the input parameters into a dict
instead of a tuple. This way, input variables can be retrieved within the function
by their name while letting the caller use a variable number of input parameters.
'''

def showArgs(*args) -> None:
    print(args) # Just print the input tuple "as is", no black magic behind the scenes.

def sumNumbers(*numbers) -> int:
    return sum(numbers) # Nothing is unpacked, thus the sum of a tuple elements (instead of independent integers)is computed.

def addNumbers(*nums) -> int:
    showArgs(*nums)             # Unpack the tuple into positional arguments and pass it to showArgs, which packs them again into a tuple.
    return sumNumbers(*nums)    # Do the same as above for sumNumbers.

def showKwargs(**kwargs) -> None:
    print(kwargs) # As **kwargs takes input parameters and packs them into a dict, this line is equivalent to printing a dict in Python.

def greet(name: str, age: int) -> None:
    print(f"Hello {name}, you are {age} years old.")

def main():
    print(f"Sum the following numbers:")
    sum_result = addNumbers(1, 2, 3, 4)
    print(f"Result: {sum_result}")
    showKwargs(name="John", surname="Doe", age=33)
    john_data = {"name": "John", "age": 33}
    greet(**john_data)

if __name__ == "__main__":
    main()