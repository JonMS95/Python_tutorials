'''
shutil module offers many high-level operations on files and directories. 
'''

from pathlib import Path
import shutil

def createDummyAssets(dir_path: str = "dummy_dir", file_name: str = "dummy_file") -> None:
    folder = Path(Path.cwd()) / dir_path
    folder.mkdir(exist_ok=True)
    file_name = folder / file_name
    with open(file_name, "w") as file:
        file.write("My name is dummy.")

def shutilUsage(new_dir_path: str, new_file_name: str, dir_path: str = "dummy_dir", file_name: str = "dummy_file") -> None:
    try:
        shutil.copytree(dir_path, new_dir_path) # Copy whole directory tree.
    except FileExistsError as fee:
        print(f"FileExistsError exception caught -> {fee}")
    except Exception as e:
        print(f"Generic exception caught -> {e}")
    
    cur_file: str = dir_path + '/' + file_name
    new_file: str = new_dir_path + '/' + new_file_name
    
    shutil.copy(cur_file, new_file) # Copy a single file.
    shutil.copy2(new_file, new_file + "_2") # Copy a single file with its metadata.
    shutil.move(new_file + "_2", new_file + "_1")  # Move file.
    # shutil.rmtree(new_dir_path)     # Remove whole tree.

def main():
    createDummyAssets()
    shutilUsage("dummy_dir_2", "new_dummy_file")

if __name__ == "__main__":
    main()