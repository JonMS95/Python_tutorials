'''
Mutability is a property of some data types in python. Basic types (int, float, str, ...) are not mutable by default.
Others (list, set, and dict) are mutable.

In Python, every variable is a reference (a name pointing to an object in memory).

x = [1, 2, 3]

In the example above, x is a label to a list somewhere in memory.

In short, "being mutable" means that the variable in question can be modified "in-place". Immutable variables,
in contrast are not modified but copied and replaced by new variables instead.

a = 1
a += 1

In the case shown above, "a" has been replaced by a new object after using += operator.
'''

import copy

def checkMemoryAddressInt():
    print("Int type variable's address changes if the variable is modified.")
    a = 1
    print(id(a))    # id shows the memory address the variable in question belongs to.
    a += 1
    print(id(a))

def checkMemoryAddressList():
    print("List are mutable, so memory address they are stored in does not change despite modfying the variable.")
    a = [1, 2, 3]
    print(id(a))
    a.append(4)
    print(id(a))

def sharedReferencesInt():
    print("When assigning an immutable type variable to other, its deeply copied (so it's a new variable with the same value).")
    a = 3
    b = a
    a += 1
    print(b)

def sharedReferencesList():
    print("If a list variable is assigned to other, a reference is shared. This way, two references are pointing at the same memory address.")
    a = [1, 2, 3]
    b = a
    a.append(4)
    print(f"a = {a}, b = {b}. Both are the same!")

def intModifier(a : int):
    a += 1

def listModifier(a : list[int]):
    if not len(a):
        a = [1]
    else:
        a.append(a[len(a) - 1] + 1)

def modifyIntIntoFunction():
    a = 1
    print(f"\'a\' before function: {a}")
    intModifier(a)
    print(f"\'a\' after function: {a}")

def modifyListIntoFunction():
    a = [1, 2, 3]
    print(f"\'a\' before function: {a}")
    listModifier(a)
    print(f"\'a\' after function: {a}")

def copyList(a : list[int]):
    b = a.copy()    # .copy() method ensures a deep copy is performed instead of simply assigning a reference to the target destination variable.
    print(f"\'a\': {a} and \'b\': {b} before deep copying \'a\' to b")
    a.append(999)
    print(f"\'a\': {a} and \'b\': {b} after deep copying \'a\' to \'b\'")

# Copies can also be performed using copy module's copy function:

def copyMatrix(a: list[list[int]]):
    b = copy.copy(a)
    print(f"\'a\': {a} and \'b\': {b} before copying \'a\' to b")
    a[0][0] *= -1
    print(f"\'a\': {a} and \'b\': {b} after copying \'a\' to b")

# copy module does also include a deep-copying function. This one copies the content of a variable recursively.

def deepCopyMatrix(a: list[list[int]]):
    b = copy.deepcopy(a)
    print(f"\'a\': {a} and \'b\': {b} before deep copying \'a\' to b")
    a[0][0] *= -1
    print(f"\'a\': {a} and \'b\': {b} after deep copying \'a\' to b")

def main():
    checkMemoryAddressInt()
    checkMemoryAddressList()
    sharedReferencesInt()
    sharedReferencesList()
    modifyIntIntoFunction()
    modifyListIntoFunction()
    copyList([1, 2, 3])
    copyMatrix([[1, 2],[3, 4]])
    deepCopyMatrix([[1, 2],[3, 4]])

if __name__ == "__main__":
    main()