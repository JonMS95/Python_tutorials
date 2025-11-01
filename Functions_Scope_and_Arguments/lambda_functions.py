'''
Lambda functions are small anonymous functions which have no name,
fit within a single line and are often used as arguments to other
functions. Syntax is pretty simple:

lambda arguments: expression

Making it basically a compact version of:
def func(arguments)
    return expression

A common use case is sorting functions. Python allows using lambda
functions with custom sorting criteria alongside both sorted
function and .sort methods.
'''

def square(x: float) -> float:
    return x ** 2

square_lambda = lambda x: x ** 2

def sortList(arr: list[str]) -> None:
    sort_crit = lambda s: len(s)
    arr.sort(key=sort_crit)

def main():
    print(f"square(2): {square(2)}")
    print(f"square_lambda(2): {square_lambda(2)}")
    words_list = ["Hello", "Bye", "John", "Hi"]
    print(f"words_list (before sorting): {words_list}")
    sortList(words_list)
    print(f"words_list (after sorting): {words_list}")

if __name__ == "__main__":
    main()