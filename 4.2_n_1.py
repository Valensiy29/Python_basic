num_f = int(input('введите первое число'))
num_s = int(input('введите второе число'))

cube = [x ** 3 for x in range(num_f,num_s + 1)]
square = [x ** 2 for x in range(num_f,num_s + 1)]

print(cube,square)