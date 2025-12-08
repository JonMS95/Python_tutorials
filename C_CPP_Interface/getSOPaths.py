from pathlib import Path as path

def getSOPath(lib_name: str) -> str:
    lib_path = path(__file__).parent / "c_lib" / "lib" / lib_name
    
    if not lib_path.exists():
        raise FileNotFoundError(f"{lib_path} does not exist!")
    
    return str(lib_path.resolve())

def getPrimeNumbersPath() -> str:
    return getSOPath("prime_numbers.so")