'''
This file provides some examples on how to handle pickle. It's extremely useful when it comes
to storing Python data (variables, class instances and so on), so it's commonly used to load
and save a given program's status.
'''

import pickle
from pathlib import Path
import time
from os import getcwd

def saveState(checkpoint_file_path: str, state: dict) -> None:
    p: Path = Path(checkpoint_file_path)

    if not p.parent.exists():
        raise FileNotFoundError(f"Path to target file does not exist ({p.parent})")
    
    with open(checkpoint_file_path, "wb") as chk_file:
        pickle.dump(state, chk_file)

def loadState(checkpoint_file_path: str) -> dict:
    p: Path =  Path(checkpoint_file_path)

    if not p.exists():
        raise FileNotFoundError(f"Target file does not exist ({checkpoint_file_path})")

    with open(checkpoint_file_path, "rb") as chk_file:
        return pickle.load(chk_file)

def main():
    checkpoint_file_path = Path(getcwd() + '/' + "dummy_checkpoint.pkl")
    state: dict = {}

    # Check if any previously saved state exists beforehand
    if checkpoint_file_path.exists():
        state = loadState(checkpoint_file_path)
        print(f"Loading state from file ({checkpoint_file_path}).")
    else:
        print(f"No checkpoint file exists, storing it in {checkpoint_file_path} from now on")
        state = {
            "counter"   : 0,
            "total"     : 0,
        }

    # Simulate some work

    for i in range(5):
        state["counter"] += 1
        state["total"] += state["counter"]

        print(f"Counter: {state['counter']}, Total: {state['total']}")

        time.sleep(1)

        saveState(checkpoint_file_path, state)

if __name__ == "__main__":
    main()
