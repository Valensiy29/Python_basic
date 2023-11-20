strafe = input('введите строку')

for index, symbol in enumerate(strafe):
    if symbol == '~':
        print(index,end = ' ')