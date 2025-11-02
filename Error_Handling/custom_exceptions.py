'''
Custom exceptions can be defined in Python by deriving them from Exception (base) class.
The most generic type of exception may be written by simply including a "pass" statement
within the class' body.
'''

# The Exception-derived class below represents an exception to be thrown whenever an
#unexpected negative value is detected somewhere. Obviously, it may have no sense in
# a real-life example but it's suitable for educationl purposes.

class NegativeValueException(Exception):
    pass

def printName(name: str) -> None:
    print(f"name: {name}")

def printAge(age: int) -> None:
    if age < 0:
        raise NegativeValueException("Age cannot be negative!")
    print(f"age: {age}")

def getPersonData(name: str, age: int) -> dict:
    printName(name)
    ret = {}
    try:
        printAge(age)
    except NegativeValueException as nve:
        print(f"Cannot print age: {nve}")
    except Exception:
        print("Caught generic exception.")
    else:
        ret = {"Name: ": name, "Age": age}
    finally:
        print(f"Ending {getPersonData.__name__} function\'s execution.")
    return ret

def main():
    print(getPersonData("Jayden", -10))
    print(getPersonData("Joe", 25))

if __name__ == "__main__":
    main()