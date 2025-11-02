def getVowelsFromString(s: str) -> str:
    ret = ""
    for c in s:
        if c in ['a', 'e', 'i', 'o', 'u']:
            ret += c
    return ret

def getReversedString(s: str) -> str:
    return s[::-1]

def wordToUpper(s: str) -> str:
    ret = ""
    for c in s:
        if c.isalpha() and c.islower():
            ret += c.upper()
        else:
            ret += c
    return ret