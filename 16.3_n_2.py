import time
from typing import Callable

def wait(func = None,*,sec:int=1):
    time.sleep(sec)
    def coming_soon_decorator(func:Callable) -> Callable:
        def wrapped_func(*args,**kwargs):
            res = func(*args,**kwargs)
            return res
        return wrapped_func
    if func is None:
        return coming_soon_decorator
    else:
        return coming_soon_decorator(func)

@wait(sec = 2)
def result():
    return [i ** i for i in range(10)]

result()