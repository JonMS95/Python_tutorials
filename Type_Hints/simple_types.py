'''
As it may have been noticed in other chapters, Python allows type hints. This way,
fellow developers can have some more detail about how the function in question is
meant to be working (i.e., which input types should it take, what is it expected
to return).

The example below is based on leetcode's 171th problem: Excel Sheet Column Number
https://leetcode.com/problems/excel-sheet-column-number/description/
'''

class ExcelCol2Num:
    # Hints exist for orphan functions, class methods and class members 
    alpha_size: int = (ord('z') - ord('a') + 1)

    def __init__(self, ):
        print(f"Created {self.__class__.__name__} class object")

    # Takes a string (char type does not exist in Python), returns an integer.
    def getIntFromChar(self, c: str) -> int:
        return ord(c) - ord('A') + 1

    # Takes a string, returns a list of integers.
    def makeIntListFromStr(self, s: str) -> list[int]:
        ret = [0 for i in range(len(s))]
        for i in range(len(s)):
            ret[i] = self.getIntFromChar(s[i])
        return ret
    
    # Takes a string, returns an integer.
    def titleToNumber(self, columnTitle: str) -> int:
        mult = 1
        ret = 0
        for col in self.makeIntListFromStr(columnTitle)[::-1]:  # Iterate integer list in inverse order.
            ret += (col * mult)
            mult *= self.alpha_size
        return ret

def main():
    e2c = ExcelCol2Num()
    for col in ["A", "AB", "ZY", "ASD", "FXSHRXW"]:
        print(f"{col} -> {e2c.titleToNumber(col)}")

if __name__ == "__main__":
    main()