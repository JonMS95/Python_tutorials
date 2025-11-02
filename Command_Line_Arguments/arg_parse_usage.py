'''
"argparse" module usage is recommended over sys's argv since it's more handleable
and provides way more interesting features.


'''

import argparse

def main():
    parser = argparse.ArgumentParser(description="Simple CLI example")
    parser.add_argument("file_name", nargs="?", default="my_file.txt", help="File to process") # nargs leads the parameter to be inputted optionally (leading it to default).
    parser.add_argument("--verbose", action="store_true", help="Enable detailed output")

    args = parser.parse_args()

    print(f"Processing file: ", {args.file_name})
    if args.verbose:
        print("Verbose mode ON")

if __name__ == "__main__":
    main()