'''
Same as in other languages supporting OOP, Python allows class inheritance.
This way, classes can extend super classes and add some additional features.

So as to call base class' methods, "super" built-in method can be used.
'''

# Base class
class Vehicle:
    def __init__(self, brand: str):
        self.brand = brand
    
    def move(self):
        print(f"Vehicle of brand {self.brand} is moving!")

# Derived class
class Car(Vehicle):
    def __init__(self, brand: str, model: str):
        super().__init__(brand)   # Call base class' init method,
        self.model = model      # then do something else.
    
    def mode(self): # Override parent method.
        print(f"The {self.brand} {self.model} is driving smoothly!")

def main():
    chevy = Car("Chevrolet", "Impala")
    chevy.move()

if __name__ == "__main__":
    main()