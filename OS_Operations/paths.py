'''
There are many ways to perform path-related ops in Python. Some of them are brought
by os and pathlib libraries, being the latter the most recent and recommended.
Only some of the available operayions will be covered in the current chapter (the
numbr of methods comprised within these libraries is actually great).
'''

import os
from pathlib import Path

def pathsWithOS() -> None:
    print(os.getcwd())  # Retrieve current working directory.
    os.makedirs("data/folder", exist_ok=True)   # Make directories.
    print(os.listdir("..")) # List files/folders.
    # os.rename("example.txt", "data/example.txt")  # Rename files (not called in this case so as not to create additional files).

def pathsWithPathlib() -> None:
    p = Path(".")
    print(p.exists())
    print(p.parent)
    print(p.absolute())
    print(p.home())
    folder = Path("data/folder")
    file_path = folder / "test.txt"
    file_path.write_text("Hello from test file!\r\n")
    file_path.rename("dummy.txt")

def main():
    pathsWithOS()
    pathsWithPathlib()

if __name__ =="__main__":
    main()
