'''
Custom exceptions can be defined in Python by deriving them from Exception (base) class.
The most generic type of exception may be written by simply including a "pass" statement
within the class' body.
'''

# The Exception-derived class below represents an exception to be thrown whenever an
#unexpected negative value is detected somewhere. Obviously, it may have no sense in
# a real-life example but it's suitable for educationl purposes.

class NegativeValueException(Exception): # This syntax stands for classes extending others (NegativeValueException extends Exception class in this case).
    pass

# Custom exceptions can be a bit more complex by calling base class' (Exception) __init__ method explicitly.

class NameTooLongException(Exception):
    def __init__(self, value, max_allowed):
        self.value = value
        self.max_allowed = max_allowed
        super().__init__(f"Current length ({value}) exceeds the maximum allowed ({max_allowed}).")

def printName(name: str) -> None:
    max_name_len = 10 
    if len(name) > max_name_len:
        raise NameTooLongException(len(name), max_name_len)
    print(f"name: {name}")

def printAge(age: int) -> None:
    if age < 0:
        raise NegativeValueException("Age cannot be negative!")
    print(f"age: {age}")

def getPersonData(name: str, age: int) -> dict:
    ret = {}
    try:
        printName(name)
        printAge(age)
    except NegativeValueException as nve:
        print(f"Cannot print age: {nve}")
    except NameTooLongException as ntle:
        print(f"Name is too long: {ntle}")
    except Exception:
        print("Caught generic exception.")
    else:
        ret = {"Name: ": name, "Age": age}
    finally:
        print(f"Ending {getPersonData.__name__} function\'s execution.")
    return ret

def main():
    print(getPersonData("Jayden", -10))
    print(getPersonData("Mary Elizabeth", 33))
    print(getPersonData("Joe", 25))

if __name__ == "__main__":
    main()