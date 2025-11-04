from print_and_call_fn import printAndCallFn

def slowWordToLen(words: list[str] = ["apple", "cherry", "banana"]) -> dict[str, int]:
    ret = {}
    for word in words:
        ret[word] = len(word)
    return ret

def wordToLen(words: list[str] = ["apple", "cherry", "banana"]) -> dict[str, int]:
    return {word: len(word) for word in words}

def conditionalWordToLen(words: list[str] = ["apple", "cherry", "banana"]) -> dict[str, int]:
    return {word: len(word) for word in words if 'a' in word}

def slowMakeHist(numbers: list[int] = [1, 3, 2, 2, 4, 3, 2, 5, 1]) -> dict[int, int]:
    ret = {}
    for number in numbers:
        if number not in ret.keys():
            ret[number] = 0
        ret[number] += 1
    return ret

def makeHist(numbers: list[int] = [1, 3, 2, 2, 4, 3, 2, 5, 1]) -> dict[int, int]:
    return {number: numbers.count(number) for number in set(numbers)}   # Redundant call counts are avoided by casting list to set.

def callDictCompFns():
    printAndCallFn(wordToLen)
    printAndCallFn(conditionalWordToLen)
    printAndCallFn(slowMakeHist)
    printAndCallFn(makeHist)