'''
Syntax is pretty simple:

def functions_name(input_variable: variable_type = default value) -> return_type:
    # Do things here
    return return_type_variable

Functions must have a function body mandatorily. If no function is defined yet, "pass" keyword can be used.
Such "pass" statement does nothing but it fills the empty space in the function's body. 

Function overloading is not allowed in Python.
'''

# Input/Output variable types do not have to be defined but it's strongly recommended (especially for those
# who have previously studied strongly typed programming languages).

def getGreet(name: str = "John") -> str:
    return ("Hello " + name + "!")

def unknownFunction() -> None:
    pass

def printSum(a, b):
    print(f"a + b: {(a + b)}")

def main():
    print(getGreet())
    unknownFunction()
    printSum(2, 3)

if __name__ == "__main__":
    main()