'''
In Python, a file can be opened by simply calling "open" function + specifying the opening type (r goes for reading).

However, opening by simply using "open" function may lead to unexpected failure, especially when leaving a file open.
Luckily, Python lets us use context handlers that can be invoked by using "with" keyword.
'''

path_to_sample_read_file = "data.txt"

def openFile(path: str) -> None:
    file = open(path, "r")
    content = file.read()
    print(content)
    file.close()

# Use context handlers for a safer handling.

def openFileSafely(path: str) -> None:
    with open(path, "r") as file:
        content = file.read()
        print(content)
    # file.close() is automatically called afterwards.