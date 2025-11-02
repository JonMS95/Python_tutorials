'''
This module covers the somewhat "archaic" way of parsing input parameters.
This tool is part of the built-in "sys" module.

For isntance, this module would require something like:

python3 sys_argv.py dummy_parameter

For it to display any input parameter apart from the program's name (0th input parameter, same as in C/C++/Bash).
'''

import sys

def main():
    input_args = sys.argv
    
    print("program\'s name (0th parameter): ", input_args[0])

    if(len(input_args) > 1):
        print("All input arguments: ", sys.argv)
    else:
        print("No input parameters were received upon the current program\'s execution.")

if __name__ == "__main__":
    main()