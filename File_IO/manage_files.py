from opening_files import path_to_sample_read_file as read_file, openFile, openFileSafely
from writing_files import path_to_write_file as write_file, createFile, overwriteFile, appendToFile
from reading_files import *

def main():
    openFile(read_file)
    openFileSafely(read_file)
    createFile(write_file)
    overwriteFile(write_file, "This is a new line\n")
    appendToFile(write_file, "This is another line\n")
    print(f"readWholeFile({write_file}): {readWholeFile(write_file)}")
    print(f"getFileLines({write_file}): {getFileLines(write_file)}")

if __name__ == "__main__":
    main()