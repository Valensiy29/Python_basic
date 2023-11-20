numbers = int(input('введите целое число'))

num = dict()

for i in range(1,numbers+1):
    num[i] = i ** 2
print(num)