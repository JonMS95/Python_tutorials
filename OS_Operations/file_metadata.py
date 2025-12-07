'''
File metadata can be retrieved in Python by using pathlib or os libraries.
'''

from pathlib import Path as path
from os import system as ossys
from os import stat as osstat, stat_result

def createDummyFile(file_path: str = "dummy_file") -> None:
    ossys(f"touch {file_path}")

def getFileStats(file_path: str = "dummy_file") -> list[stat_result]:
    ret: list[stat_result] = []

    try:
        f = path(file_path)
        ret.append(f.stat())            # Pathlib stat
        ret.append(osstat(file_path))   # os.stat
    except FileNotFoundError as fnfe:
        print(f"Caught FileNotFoundError exception: {fnfe}")
    except Exception as e:
        print(f"Caught generic exception: {e}")

    return ret

def main():
    createDummyFile()
    stats = getFileStats()

    if stats:
        print(stats[0])
        print(stats[1])

if __name__ == "__main__":
    main()
