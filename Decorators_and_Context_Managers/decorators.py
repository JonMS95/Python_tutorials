'''
Decorators are functions that return wrapper functions. Such wrapper functions are meant
to run some code before and after a target function. See the example below for a better
understanding.
'''

'''
The function below will return a function (called wrapper in this case), which will operate
with decorator-provided fn function. Therefore, the function it will return is equivalent to:

(Assume myDecorator(myFunction))

def wrapper(*args, **kwargs)
    print(f"Before running {myFunction.__name__}")
    ret = myFunction(*args, **kwargs)
    print(f"After running {myFunction.__name__}")

Therefore, a per-function-customized wrapper function will be returned in each case.

Note that wrapper takes args and kwargs as input parameters so everything being passed to
wrapped function is forwarded to the wrapper.
'''

def myDecorator(fn):
    def wrapper(*args, **kwargs):
        print(f"Before running {fn.__name__}")
        ret = fn(*args, **kwargs)
        print(f"After running {fn.__name__}")
        return ret
    return wrapper

'''
Using my @myDecorator as below is equivalent to doing this manually:

sayHello = myDecorator(sayHello)

Again, the sayHello assignment above would be equal to the following custom function:

def wrapper(*args, **kwargs):
    print(f"Before running {sayHello.__name__}")
    ret = sayHello(*args, **kwargs)
    print(f"After running {sayHello.__name__}")
    return ret

So we can tell that wrapper functions takes everything that's passed to sayHello, then
calls sayHello by using all of those input parameters.
'''

@myDecorator
def sayHello(name) -> None:
    print(f"Hello {name}!")

def main():
    sayHello("Alice")

'''
The line above is equivalent to:

wrapper("Alice")
'''

if __name__ == "__main__":
    main()