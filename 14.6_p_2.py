import time
from typing import Callable


def coming_soon(func:Callable) -> Callable:
    time.sleep(3)
    def wrapped_func(*args,**kwargs):
        if func == func:
            return 'all good'
        else:
            return 'all bad'
    return wrapped_func

@coming_soon
def result():
    return [i ** i for i in range(10)]

result()