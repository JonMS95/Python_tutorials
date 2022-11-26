class Programmer():
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def __str__(self):
        return "Hello, my name is " + self.name + " and I'm " + str(self.age) + " years old."

    name = "Jon"
    age = 27
    
    def develop(self):
        print("Writing code...")
    
    def changeName(self, newName):
        self.name = newName
    
    def changeAge(self, newAge):
        self.age = newAge