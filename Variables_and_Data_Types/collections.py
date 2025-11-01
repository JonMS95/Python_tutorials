'''
Python has four core built-in collections:

·list: mutable, ordered, changeable list of numbers.    [1, 6, 2, 9]
·tuple: immutable, ordered, fixed list of numbers.      (4, 2, 8)
·set: mutable, unordered set of unique numbers          {7, 3, 2}
·dict: mutable key-value mapping structure.             {"name": "Alice", "age": 30}
'''

def main():
    data = [1, 2, 3]
    data.append(4)
    print(f"data: {data}")

    coords= (10, 20)
    print(f"coords[0]: {coords[0]}")

    # Note that repeated values will not be inserted once again, so a single "2" will exist within the set below.
    unique_values = {1, 3, 2, 5, 2}
    print(f"unique_values: {unique_values}")

    person = {"Name": "Bob", "Age": 45}
    print(f"person: {person}")

if __name__ == "__main__":
    main()