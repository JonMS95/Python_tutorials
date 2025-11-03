'''
Control structures may look cleaner and more readable than in C/C++,
but they are conceptually the same. These are the types of control
structures in Python:

·if-elif-else
·comparison and logical
·for loops
·while loops
·break
·continue
·for...else
·while...else
·match...case (Python >=3.10)
'''

def getAgeRange(age: int) -> str:
    if age <= 18:
        return "Child"
    elif 19 <= age <= 35:   # Equivalent to: age >= 19 and age <= 35
        return "Youngster"
    else:
        return "Oldie but goldie"

days_in_ger_eng = [
    ["Montag"       , "Monday"      ],
    ["Dienstag"     , "Tuesday"     ],
    ["Mittwoch"     , "Wednesday"   ],
    ["Donnerstag"   , "Thursday"    ],
    ["Freitag"      , "Friday"      ],
    ["Samstag"      , "Saturday"    ],
    ["Sonntag"      , "Sunday"      ],
]

def printDays():
    for couple in days_in_ger_eng:  # Elements can be retrieved without using their indexes (same as for(int n: vec_int) syntax in C++)
        print(f"{couple[0]} -> {couple[1]}")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

def printDaysAsMatrix():
    for i in range(len(matrix) - 1, -1, -1): # Elements within an iterable data structure can also be iterated by using indexes: range([start, end), step).
        for j in range(0, len(matrix[i]), 1):
            print(matrix[i][j], end="")
        print()

def printPositiveNumbers(n: int = 10) -> None:
    while n > 0:
        print(f"{n} ", end="")
        n -= 1
    print()

def printEvenNumbers(n: int = 10) -> None:
    for i in range(n):
        if i < 0:
            break
        if i % 2 == 0:
            print(f"{i} ", end="")
        else:
            continue
    print()

def findFirstEvenNumber(a: int, b: int) -> None:
    for n in range(a, b):
        if n % 2 == 0:
            print("Found even: ", n)
            break
    else:
        print("No even number found")

def https_status(code: int) -> str:
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _: # Default case
            return "Unknown"

def main():
    getAgeRange(25)
    printDays()
    printDaysAsMatrix()
    printPositiveNumbers()
    printEvenNumbers()
    findFirstEvenNumber(2, 10)
    print(f"https_status(404) -> {https_status(404)}")

if __name__ == "__main__":
    main()