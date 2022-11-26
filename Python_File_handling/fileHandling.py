# If any doubt about what's going on here (regarding scryp module's usage), check the "Python_Modules" tutorial.

from scryp import encrypt, decrypt

from fileHandling_constants import *

# To open a file, var = open("pathToFile", "mode") type sentence should be used.
# Here, "pathTofile" can be substituted by the file's name if it's found in the same directory as the python script.
# "mode" stands for the mode the file is meant to be opened:
#     "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#     "a" - Append - Opens a file for appending, creates the file if it does not exist
#     "w" - Write - Opens a file for writing, creates the file if it does not exist
#     "x" - Create - Creates the specified file, returns an error if the file exists
#
# Keep in mind that every argument of the function should be passed as a string. The function returns a string as
# well (when reading).
# In addition, it can be specified if the file is willing to be handled as binary or text mode. Use "rt" instead
# of just "r", for example.
#     "t" - Text - Default value. Text mode
#     "b" - Binary - Binary mode (e.g. images)

# Despite of having the ability to pass the name of the target file to the "open" function, the whole path to it
# is going to be used, as it's considered to be more general-purpose-friendly. 
f = open(PATH_STRANGE_MAN, "r")

firstLine = f.read()
print(firstLine)
print(f.read())

# It's a good practise to close each file after using it. Sometimes, errors due to buffering may occur.
f.close()

# From the python's point of view, a file is something like an array of strings. Thus, it can be iterated as that.
f = open(PATH_FIRE, "r")

for line in f:
    print(line)

f.close()
print()

# Let's append a line to a file now:
appendFile = open(PATH_STRANGE_MAN, "a")
appendFile.write(LINE_BLACKWATER)
appendFile.close()

# A new file is going to be created as the following line is executed. If the file already exists, it's going to be
# overwritten. 
writeFile = open(PATH_I_KNOW_YOU, "w")
f = open(PATH_STRANGE_MAN, "r")
for line in f:
    writeFile.write(encrypt(line, PASSWORD) + "\n")

writeFile.close()
f.close()

# Finally, the encrypted text file that has just been created is going to be read and decrypted line by line:
decrypted = open(PATH_I_KNOW_YOU, "r")
for line in decrypted:
    print(decrypt(line, PASSWORD))