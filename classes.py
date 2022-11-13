# Class declaration syntax in Python.

# class ClassName:
#     functions
#     variables

# "self" keyword is used to references variables or methods within the current class. It's a reference to the
# current instance of the class, and it's used to access variables that belong to the class.
# "self" name is just a convention, it can be called in any other way. It should always be there.

class Person:
    def __init__(self, name, age):
        self.name   = name
        self.age    = age

    def __str__(self):
        return f"My name is {self.name}, and I'm {self.age} years old."

    def reverse(self, input_str):
        ret = ""
        for i in range(len(input_str) - 1, -1, -1): # From the last index of the string, while index > -1, step = -1. 
            ret += input_str[i]
        return ret

p1 = Person("John", 36)
print(f"Name:\t{p1.name}\r\nAge:\t{p1.age}")

# Class attributes may be modified, same as ordinary variables:
p1.name = "Jon"
p1.age  = 27
print(p1)

print(p1.reverse("Yes"))

# Object properties (attributes) may be deleted.
# Once it's done, they cannot be referenced again as they no longer exist.

del p1.name

# The line below will lead the program to a runtime error, so it's will stay commented.
# print(p1.name)

# Classes may have no content at all, but their body can't be empty,
# so at least "pass" statement should exist within it.

class EmptyClass:
    pass

# Inheritance works in a pretty similar way as it does in C++. Once a class is declared to be
# inheritor of another one, all of the methods and properties will exist in it. Additionally,
# some other data could be described for the child class.
# Methods could be easily overriden.
# There's no need to type any specific keyword, just write the definition. If what is wanted
# is to use a method from the parent class, "super()" method should be called.

class Inheritor(Person):
    def __init__(self, inputName, inputAge, inputJob):
        super().__init__(inputName, inputAge)
        self.job = inputJob

    def defineJob(self, jobName):
        self.job = jobName

# In this case, the constructor (__init__) method will use first the parent class __init__ method, and then
# it will perform any other additional actions (setting the job attribute's value in this case).

i1 = Inheritor("Jon", 27, "Computer scientist")
print(i1.reverse(i1.name))

# There's something that hasn't been talked about yet: access operators. In Python, every memeber of a class
# is public by default, it's to say, it can be seen or modified by any other entity. However, there are some
# ways in which privacy could be modified for those members.

# Protected members of a class are the ones that are only visible for the class itself, as well as for the
# inheritor classes. A variable in conventionally declared protected by defining its name starting with an
# underscore. Keep in mind that it's only a convention, so it doesn't make the variable actually protected.
# Commonly, @property decorator should be used. To make them private, a double underscore should be used
# before typing the actual name of the variable.

class AccessExample:
    def __init__(self, inputAge, inputName):
        self._age   = inputAge
        self._name  = inputName
        self.__sth  = "Something"

ae1 = AccessExample(27, "Jon")
print(ae1._name)

def Try2ChangePE(object):
    object._age = 0

Try2ChangePE(ae1)
print(ae1._age)

ae1.__sth = "Wow!"
print(ae1.__sth)

# A remarkable (and maybe disappointing too) fact about Python is that access is never modified,
# no matter which naming convention or decorators are used. Whatever is written surrounding the
# target variable doesn't affect its privacy, so it will remain public.