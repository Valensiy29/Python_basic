import time
from typing import Callable
from datetime import datetime


def log_methods(format):
    def decorator(cls):
        def wrapped_loger(*args,**kwargs):
            start = time.time()
            instanse = cls(*args,**kwargs)
            end = time.time()
            print('запускается',instanse,':\n','время создания класса',datetime.utcnow(),'время работы ',end - start)
            return instanse
        return wrapped_loger
    return decorator


@log_methods("b d Y — H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")
    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()