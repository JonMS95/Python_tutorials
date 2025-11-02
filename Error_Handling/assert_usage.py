'''
"assert" keyword usage is a simple way to state conditions that should be met
so as not to raise any exception. If any unexpected condition is caught, then
an AssertionError is raised. A message to initialize such exception with can
be provided optionally.

Syntax is pretty much straightforward:

assert <condition>, "Error message to initialize AssertionError with"

or simply:

assert <condition>
'''

def canEnterTheClubAssert(age: int) -> bool:
    assert age > 0 and age <= 100, "Age is out of range"
    return age >= 18 and age <= 30

def isNameLongEnoughAssert(name: str) -> bool:
    assert len(name) > 0, "No name has been provided"
    return len(name) > 3

def canEnterTheClub(age: int) -> bool:
    ret = False
    try:
        ret = canEnterTheClubAssert(age)
    except AssertionError as ae:
        print(f"Assertion error caught: {ae}")
    finally:
        return ret

def isNameLongEnough(name: str) -> bool:
    ret = False
    try:
        ret = isNameLongEnoughAssert(name)
    except AssertionError as ae:
        print(f"Assertion error caught: {ae}")
    finally:
        return ret

def main():
    print(f"canEnterTheClub(-1): {canEnterTheClub(-1)}")
    print(f"canEnterTheClub(110): {canEnterTheClub(110)}")
    print(f"canEnterTheClub(25): {canEnterTheClub(25)}")
    print(f"canEnterTheClub(37): {canEnterTheClub(37)}")
    print(f"isNameLongEnough(''): {isNameLongEnough('')}")
    print(f"isNameLongEnough('John'): {isNameLongEnough('John')}")

# Tip: when interpolating strings, alternate double and single quotes. Otherwise, interpreter may not know where does the formatted string actually end.

if __name__ == "__main__":
    main()