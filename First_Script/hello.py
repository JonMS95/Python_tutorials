'''
Use:

·def: to define a function.
·print: outputs to the terminal.
·input: reads a string from standard input.
·f"Welcome, {name}!: interpolates a string.
·if __name__ == "__main__": ensures the code only runs if the file is executed directly (not imported).
·main(): calls main function.
'''

def main():
    print("Hello Python")
    name = input("What's your name? ")
    print(f"Welcome, {name}! Let's master Python together.")

if __name__ == "__main__":
    main()