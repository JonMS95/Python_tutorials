'''
Environment variables can be modified using os library.
'''

from os import environ as oe

def createEnvVars(var_name: str, var_val: str) -> None:
    oe.environ[var_name] = var_val
