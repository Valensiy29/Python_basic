s = input('Введите строку: ')
sym_num = int(input('Номер символа: '))
pos_sym = sym_num
sym = list(s)
for index,i in enumerate(sym):
    if index == sym_num:

        print(sym[index])

        print(sym[sym_num - 2])