'''
Again, os library can be used for CLI commands to be executed.
'''

from os import system as ossys
from subprocess import run as rs

'''
os.system is the legacy choice. Nice, but constrained to running simple commands.
'''
def runOSSystemCommands() -> None:
    ossys("echo Hello from shell!")
    ossys("ls .")

'''
subprocess is a newer alternative. Captures output, arguments, return codes and handles errors.
'''
def runSubprocessCommands(cmd: str, args: str) -> str:
    return rs([cmd, args], capture_output=True, text=True)

def main():
    runOSSystemCommands()
    print(runSubprocessCommands("ls", "-alF"))

if __name__ == "__main__":
    main()