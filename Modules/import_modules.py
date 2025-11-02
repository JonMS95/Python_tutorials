'''
In python, there are many ways of importing modules into a file:
·import (plain import): just imports the whole file including all of its symbols.
    This involves importing symbols with module.symbol syntax.
·import module_name as alias: imports a module with an alias. Typical example: import pandas as pd.
    Symbols are imported with the following syntax: alias.symbol
·from module import symbol: imports just a symbol (or symbols) from a module. "from module import symbol_1, symbol_2" also works for multiple symbols.
    Use symbols by simply calling them.
·from module import symbol as alias: imports a symbol from a module under an alias.
    Call symbols simply naming them same as in the prior example.
·from module import *: not recommended since it imports every symbol separatedly.
'''

import math_module
import histogram_module as hist_mod
from strings_module import wordToUpper
from strings_module import getReversedString as getRevStr

def main():
    print(f"4 + 2 = {math_module.add(4, 2)}")
    print(f"4 - 2 = {math_module.sub(4, 2)}")
    test_list = [1, 4, 2, 7, 8, 4, 1, 4]
    print(f"{test_list} -> {hist_mod.makeHistogramFromList(test_list)}")
    test_str_0 = "My name is Bob and I'm 33 years old."
    print(f"{test_str_0} -> {wordToUpper(test_str_0)}")
    test_str_1 = "Lorem ipsum dolor sit amet"
    print(f"{test_str_1} -> {getRevStr(test_str_1)}")

if __name__ == "__main__":
    main()