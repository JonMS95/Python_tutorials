'''
An exception is an event that interrupt the normal flow of a program when
something goes wrong unexpectedly.

Example:

x = int("Hello")

The line above will lead to a runtime error since strings cannot be casted
to integers whatsoever.

The syntax is pretty similar to C++'s:

try:
    <Code to be tested>
except error_type_0:
    <Code to execute after catching error_type_0>
except error_type_1:
    <Code to execute after catching error_type_1>
...
except Exception:
    <Code to execute after catching generic error type>
else:
    <Code to be executed in case no exception was caught>
finally:
    <Code to be executed in any case (good for cleanup)>

"try" and "except" blocks are mandatory. Since "except" blocks are iterated
from first to last, it's strongly recommended to order them in "genericness"
order, being "Exception" the base class (i.e., the most generic exception
type). Also, aliases can be set for exceptions so that they are retrieved
when caught:

except exception_type as e_type:

"else" and "finally" blocks are optional. The prior includes teh code to
execute in case everything went OK, the latter is always executed.

Custom expections can be thrown by using "raise" keyword.

For us to know what exception types do exist, check official docs.
'''

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return (a / b)

def tryToDivide(a: float, b: float) -> None:
    ret = 0
    try:
        ret = divide(a, b)
    except ValueError as val_err:
        print(f"Error caught while trying to divide {a} by {b}: {val_err}")
    except Exception:
        print("Generic exception caught.")
    else:
        print(f"{a} / {b} = {ret:.3f}")
    finally:
        print(f"Ended {tryToDivide.__name__}\'s execution.")

def main():
    tryToDivide(10, 0)
    tryToDivide(5, 3)

if __name__ == "__main__":
    main()