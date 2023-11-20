import random
delit = 0
num = int(input('длина списка'))
spis = [random.randint(0,num) for i in range(num)]
number = []
for i in spis:
    if i % 2 == 0:
        number.append(1)
    else:
        i %= 5
        number.append(i)

print(number)