def func_2(func_1,num):

    return func_1(num) * func_1(num)


def func_1(x):
    return x + 10

print(func_2(func_1, 9))