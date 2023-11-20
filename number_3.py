
def num_count(number):
    result = 1
    while number % 10 <= 0:
        number %= 10
        result += 1
    print('количество цифр в числе: ',result)
def num_sum(num):
    result = 0
    sum = 0
    while num > 0:
        sum = sum + num % 10
        num = num // 10
    print('сумма цифр числа',sum)
    num_2 = num_count(number)
    result += sum - num_2
    print(result)


number = int(input(''))
num_count(number)
num_sum(number)
