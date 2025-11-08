'''
When using generator expressions, "yield" keyword can be used so as to
generate new elements lazily. "yield" keyword does something similar to
saving function's status before returning. It's something like a
checkpoint.

Every function that comntains yield becomes a generator, returning a
generator object instead of immediately returning a final value. 
'''

# Returns a generator expression.
def countdown(n: int):
    print("Starting countdown...")
    while n > 0:
        yield n # Pauses here
        n -= 1

'''
The function above (countdown) returns a generator. In this case,the
generator would be equivalent to returning the following:
return (n for n in range(n, -1, -1))
'''

# Returns a list.
def normalCountdown(n: int):
    ret = []
    for i in range(n, 0, -1):
        ret.append(i)
    return ret