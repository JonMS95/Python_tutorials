# Same as it's done in C with "#include fileName" statements, "import fileName" is used in Python.
import myModule

# It's also possible to import a module with an alias, which is usually done for the sake of understandability.
import myModule2 as classModule

# Python has a large number of built-in modules. These can also be imported.
# The one below, for example, provides the methods that are necessary to perform a binary search.
import bisect

# If only a symbol is meant to be imported, then the "from moduleName import symbolName" syntax should be followed.
# Then, the module name has no longer need to be mentioned.
from myModule3 import toUpperCase

print(myModule.reverseString(myModule.aboutMe["Birthplace"]))

littleProgrammer = classModule.Jon()

# Note that some methods do not need to be imported, such as sort(). 
myModule.aboutMe["RandomList"].sort()

# In this case, the list is first printed, then the target value (2) is found.
print(myModule.aboutMe["RandomList"])
print(bisect.bisect_right(myModule.aboutMe["RandomList"], 2))

# If the aim is to list all of the names (variables + functions) in a module, dir(moduleName) function may be used.
print(dir(myModule))

print(toUpperCase(littleProgrammer.name))