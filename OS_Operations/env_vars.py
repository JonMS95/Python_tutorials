'''
Environment variables can be modified using os library.
'''

from os import environ as oe

def createEnvVars(var_name: str, var_val: str) -> None:
    oe[var_name] = var_val

def getEnvVarValues(*env_vars):
    for var in env_vars:
        print(f"{var} -> {oe.get(var)}")

def main():
    createEnvVars("MONTY", "PYTHON")
    getEnvVarValues("MONTY", "HOME")

if __name__ == "__main__":
    main()