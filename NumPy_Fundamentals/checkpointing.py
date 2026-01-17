'''
This chapter is not about math but rather about engineering discipline. Checkpointing is
a NumPy feature (it's also featured in common Python) that allows us to save the status
of a program so that it can be backed up so as to continue later with it or simply to
save critical data.

Similar to picle, .save and .load functions are used whe in NumPy, being .npy its format.
Use .savez and .savez_compressed for multiple arrays, the result will be stored within a
.npz file.

It's commonly used when computations are expensive, crahes may occur and results matter.
'''

import numpy as np
from pathlib import Path
from os import getcwd

def saveArray(A: np.ndarray, target_npy_path: str = (getcwd() + "/dummy_matrix.npy")) -> None:
    p: Path = Path(target_npy_path)

    if not p.parent.exists():
        raise FileNotFoundError(f"Path to target file cannot not exist ({p.parent})")
    
    np.save(target_npy_path, A)

def loadArray(path_to_npy: str) -> np.ndarray:
    p: Path = Path(path_to_npy)

    if not p.exists():
        raise FileNotFoundError(f"Path to target file does not exist ({p})")

    return np.load(path_to_npy)

def saveMultipleArrays() -> None:
    A: np.ndarray = np.array([_ for _ in range(9, 0, -1)])
    B: np.ndarray = np.array([_ for _ in range(1, 10)]).reshape(3, 3)
    np.savez(getcwd() + "dummy_multiple.npz", x = A, y = B)
    np.savez_compressed(getcwd() + "dummy_multiple_compressed.npz", x = A, y = B)

def storeWithMetadata(A: np.ndarray, target_npy_path: str = (getcwd() + "/dummy_matrix_with_metadata.npy")) -> None:
    p: Path = Path(target_npy_path)

    if not p.parent.exists():
        raise FileNotFoundError(f"Path to target file cannot not exist ({p.parent})")

    details = {
        "version": 1,
        "description": "Simulation output",
        "dtype": str(A.dtype),
        "shape": A.shape
    }

    np.savez(target_npy_path, A = A, metadata = details)

def main():
    X: np.ndarray = np.array([_ for _ in range(1, 17)]).reshape(4, 4)

    saveArray(X)
    print(f"Loaded array: {loadArray(getcwd() + '/dummy_matrix.npy')}")
    saveMultipleArrays()
    storeWithMetadata(X)

if __name__ == "__main__":
    main()