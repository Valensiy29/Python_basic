import random
sum = 0
with open('res.txt', 'a') as file:
    while sum < 777:
        number = int(input(''))
        sum += number
        luck = random.randint(1,13)
        file.write(str(number))
        if luck == 1:
            break

