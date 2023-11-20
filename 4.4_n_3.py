import random
#
# num = int(input('какой длины будет список?'))
# num_2 = int(input('с какого числа срез'))
# number = int(input('по какое'))
# count = [i for i in range(num)]
# count_2 = count[:]
# count_2[num_2:number]
n = int(input("Введите количество чисел N: "))

numbers = [random.randint(-10, 10) for _ in range(n)]

a = random.randint(0, len(numbers) - 2)
b = random.randint(a + 1, len(numbers) - 1)
# Генерируем числа так, чтобы они не выходили за границу списка
print(numbers, a, b)
numbers = numbers[:a] + numbers[b + 1:]
print(numbers)