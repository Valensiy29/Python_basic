def sum(*args):
    sum = 0
    numbers = args[:]
    for ind,num in enumerate(numbers):
        if isinstance(num,list):
            for i,nu in enumerate(numbers[ind]):
                sum += i
                if isinstance(nu,list):
                    sum += numbers[ind][0][i]
                elif isinstance(numbers[ind][i], list):
                    sum += 1
        else:
            sum += numbers[ind]
    return sum

# numbers = input('напишите числа через запятую').split(',')
# num = [int(x) for x in numbers]
sum([[1, 2, [3]], [1], 3])