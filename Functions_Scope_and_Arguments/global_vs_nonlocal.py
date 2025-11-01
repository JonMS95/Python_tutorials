'''
Two keywords allow functions in python modify variables that can exist in a different scope:

·global: modify a global variable.
nonlocal: modify a variable from an outer (enclosing) function scope.
'''

count = 0 # Global variable.

def increment():
    global count # The intention to use the global variable is declared here.
    count += 1
    print(f"count: {count}")

def outer():
    x = 5

    def inner():
        nonlocal x
        x += 1
        return x
    
    print(f"inner(): {inner()}")

def main():
    increment()
    outer()

if __name__ == "__main__":
    main()