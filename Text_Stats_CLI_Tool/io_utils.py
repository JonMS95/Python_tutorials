from pathlib import Path

def getFileLines(file_path: str) -> list[str]:
    target_file_path = Path(file_path)
    
    if not target_file_path.exists():
        raise FileNotFoundError(f"Could not find {file_path}")

    with open(file_path, 'r') as file:
        return file.readlines()
