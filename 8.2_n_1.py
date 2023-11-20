import math


def rec_factorial(number):
    if number <= 1:
        return 1
    else:
        return number * rec_factorial(number - 1)


n = 1000
print(rec_factorial(n), math.factorial(n), rec_factorial(n) == math.factorial(n))