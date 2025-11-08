'''
Here goes an example showcasing a common decorator use case: function timing.
In this case, a wrapper will be generated in such way that when the target
function is called:

1 - Current time and date will be stored in a variable ("time" module will
be to fulfil such task).
2 - Target function will be executed.
3 - Time difference (using previously stored initial time as reference) will be
calculated and returned.
'''

from time import time as getCurTime

def timingDecorator(target_fn):
    def wrapper(*args, **kwargs):
        start_time = getCurTime()
        ret = target_fn(*args, **kwargs)
        end_time = getCurTime()
        print(f"{target_fn.__name__} functions\'s execution took {(end_time - start_time):.2f} seconds")
        return ret
    return wrapper

'''
The decorator above will be used in another module. Please, note that they are
nothing but common functions that will be placed just before another function's
definitions so they are called by the wrapper within.
'''