'''
Every object in Python has it's very own identity (e.g., it's memory address).
Use id() to inspect it.
'''

def main():
    x: list[int] = [1, 2, 3]
    y = x
    z = [1, 2, 3]

    # Id's for x and y will be the same since they are both pointing at the same memory address.

    for key, value in {"x": x, "y": y, "z": z}.items():
        print(f"id({key}): {id(value)}")
    
    print(f"id(x) == id(y): {id(x) == id(y)}")
    print(f"id(x) == id(z): {id(x) == id(z)}")

    # Same as Java, Python interns small integers short strings for the sake of efficiency. This way
    # immutable objects can be referenced as lists or tuples (among others). 

    a = 256
    b = 256

    print(f"a is b: {a is b}")

    c = "Hello"
    d = "Hello"

    print(f"c is d: {c is d}")


if __name__ == "__main__":
    main()