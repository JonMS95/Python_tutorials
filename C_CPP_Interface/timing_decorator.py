from time import time as getCurTime

def timingDecorator(target_fn):
    def wrapper(*args, **kwargs):
        start_time = getCurTime()
        ret = target_fn(*args, **kwargs)
        end_time = getCurTime()
        
        print(f"{target_fn.__name__} functions\'s execution took {(end_time - start_time):.2f} seconds")
        
        return ret
    return wrapper