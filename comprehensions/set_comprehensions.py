from print_and_call_fn import printAndCallFn

def countUniqueLengths(words: list[str] = ["Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit"]) -> set[int]:
    return {len(word) for word in words}

def uniqueLettersInSentence(sentence: str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.") -> set[str]:
    return {letter for letter in sentence if letter.isalpha()}

def callSetCompFns():
    printAndCallFn(countUniqueLengths)
    printAndCallFn(uniqueLettersInSentence)