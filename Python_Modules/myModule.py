# In this file, a function and a dictionary that are later going to be imported in another file are defined.
def reverseString(inputStr):
    if type(inputStr) != str:
        return -1
    outputStr = ""
    for i in range(len(inputStr) - 1, -1, -1):
        outputStr += inputStr[i]
    return outputStr

aboutMe = {
    "Age": 27,
    "Name": "Jon",
    "Birthplace": "Barakaldo"
}

class Jon():
    name = "Jon"
    
    def develop(self):
        print("Writing code...")
    
    def changeName(self, newName):
        self.name = newName
    
    def changeAge(self, newAge):
        self.age = newAge