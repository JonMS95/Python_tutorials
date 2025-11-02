'''
There a re three ways to write in to a file in python, depending on the input parameter passed to open function:
·x: creates a new file only if it does not exist beforehand, leading to an error otherwise.
·w: writes to the target file by overwriting any existing content.
·a: appends tot he target file, so any content existing beforehand will remain afterwards.
'''

path_to_write_file = "file_to_write.txt"

def createFile(path_to_file: str) -> None:
    try:
        with open(path_to_file, "x") as file:
            pass
        print(f"File {path_to_file} created successfully")
    except FileExistsError:
        print(f"File {path_to_file} already exists.")

def overwriteFile(path_to_file: str, new_content: str) -> None:
    with open(path_to_file, "w") as file:
        file.write(new_content)

def appendToFile(path_to_file: str, new_content: str) -> None:
    with open(path_to_file, "a") as file:
        file.write(new_content)

def main():
    createFile(path_to_write_file)
    overwriteFile(path_to_write_file, "This is a new line\n")
    appendToFile(path_to_write_file, "This is another line\n")