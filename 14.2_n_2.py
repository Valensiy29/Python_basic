import time
def timer(func):
    def wrapped_func(*args,**kwargs):
        start = time.time()
        res = func(*args,**kwargs)
        end = time.time()
        print('время функции',end - start)
        return res
    return wrapped_func


@timer
def square_nums():
    return [i ** i for i in range(10)]

square_nums()