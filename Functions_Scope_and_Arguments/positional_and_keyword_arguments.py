'''
Despite function overloading being forbidden in Python, both positional
and keyword (named).

Positional arguments must be passed in the same order as specified in
the function in question, whereas named arguments should match the name
used alongside the function call.

However, something taht's worth pointing out is that these arguments'
types do not depend on how are functions defined but how are them called
instead.

Also, note that input parameters with default values should always be
placed last so that it's clear the value of each positional argument.
'''

def makeHistFromArgs(name: str, age: int, height: float, weight: float, is_hard_worker: bool = True) -> dict:
    return { "Name": name, "Age": age, "Height": height, "Weight": weight, "Is a hard worker": is_hard_worker}

def main():
    print(f"{makeHistFromArgs(age=33, weight=88.5, is_hard_worker=False, name='John', height=172.3)}")
    print(f"{makeHistFromArgs('Rose', 30, 165.2, 56.7)}")   # No need to provide default-valued parameter.

if __name__ == "__main__":
    main()