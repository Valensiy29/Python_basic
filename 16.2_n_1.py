import time
from contextlib import contextmanager


@contextmanager
def timer(num):
    start = time.time()
    yield num * 10
    print(time.time() - start)


with timer(10) as func:
    num = func * 100 * 1000
    print(num)
