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
    "Birthplace": "Barakaldo",
    "RandomList": [34, 1, 76, 33, 2, 0, -23, 55, -123, 1, 10]
}