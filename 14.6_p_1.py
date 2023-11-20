import time
from typing import Callable

def how_are_you(func:Callable) -> Callable:
    def wrapped_func(*args,**kwargs):
        question = input('как у тебя дела?')
        print('а у меня не очень')
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print('время функции', end - start)
        return res
    return wrapped_func



@how_are_you
def test():
    return [i ** i for i in range(10)]


test()