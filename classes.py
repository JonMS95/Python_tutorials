# Class declaration syntax in Python.

# class ClassName:
#     functions
#     variables

# "self" keyword is used to references variables or methods within the current class.

class Person:
    def __init__(self, name, age):
        self.name   = name
        self.age    = age

    def __str__(self):
        return f"My name is {self.name}, and I'm {self.age} years old."

p1 = Person("John", 36)
print(f"Name:\t{p1.name}\r\nAge:\t{p1.age}")

# Class attributes may be modified, same as ordinary variables:
p1.name = "Jon"
p1.age  = 27
print(p1)