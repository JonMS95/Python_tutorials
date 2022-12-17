# Same as in other OOP languages such as C++, lambda functions are just small anonymous functions. The syntax is as follows:
# lambda arguments : expression
x = lambda a : a + 10
print(x(5))

# Same as common functions, lambda functions accept multiple input arguments:
y = lambda a, b : a + b
print(y(4, 7))

# Lambda functions are usually defined within other functions:
def myFunc(n):
    return lambda a : a * n

# This is the same as typing: myDoubler = lambda a : a * 2. The point is the lambda function is defined each time myFunc is called.
myDoubler = myFunc(2)
myTripler = myFunc(3)

print(myDoubler(5))
print(myTripler(6))