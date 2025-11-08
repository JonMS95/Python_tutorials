'''
Generators can be chained. Remember: use yield to return a
generator expression instead of its equivalent list.
'''

def natural_numbers():
    i = 1
    while True:
        yield i
        i += 1

# Generator 2: squares numbers from another generator
def square_numbers(numbers):
    for n in numbers:
        yield n * n

# Generator expression to filter even squares and take first n of them
def first_n_even_squares(n: int):
    squares = square_numbers(natural_numbers())
    count = 0
    for sq in squares:
        if sq % 2 == 0:
            yield sq
            count += 1
            if count >= n:
                break

def main():
    print(f"list(first_n_even_squares(10)): {list(first_n_even_squares(10))}")

if __name__ == "__main__":
    main()