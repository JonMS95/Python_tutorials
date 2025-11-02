'''
Python's "open" function takes "r" as its second parameter's default value, so no need to
specify it (it can be called either as open(file_path, "r") or open(file_path)).

When it comes to reading methods once the file has already been opened, any of the following
may be used:
·.read(): read the entire file.
·.readline(): read next line.
·.readlines(): retrieve a list of all lines wtihin target file.
'''

def readWholeFile(path_to_file: str) -> str:
    with open(path_to_file) as file:
        return file.read()

def getFileLines(path_to_file: str) -> list[str]:
    with open(path_to_file) as file:
        return file.readlines()