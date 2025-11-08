'''
Python classes have some user-definable built-in methods which are
inherited from a common superclass called "object", which every
user-defined class inherits from:
·__enter__: meant to be called whenever a class object is created.
·__exit__: same but being called when the object is destroyed.
These functions overwrite the ones in the "object" superclass.

Please, note that for the methods above to be "activated", the target
object must be called by using "with" keyword.

Context managers are nothing but user-defined classes which meet some
special requirements.

Subtle aspects on class definition/creation in Python will be further
discussed on a dedicated lesson. 
'''

class myContextManager:
    def __init__(self, filename, mode = "r"):
        print(f"Preparing to open {filename}")
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("Entering context.")
        self.file = open(self.filename, self.mode)
        return self.file
    
    # Input parameters for __exit__ must be included even if not using them.
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context.")
        if self.file:
            self.file.close()
        return False

def main():
    with myContextManager("test_file.txt") as file:
        try:
            print(file.read())
        except Exception as e:
            print(f"File could not be read: {e}")

if __name__ == "__main__":
    main()