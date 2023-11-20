def calculating_math_func(data, result):
    result /= data ** 3
    result = result ** 10
    return result




data= int(input('введите число'))
result = 1
for index in range(1, data + 1):
    result *= index
calculating_math_func(data, result)