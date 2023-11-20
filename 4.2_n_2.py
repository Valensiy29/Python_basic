strafe = input('введите строку')
symbol = input('введите символ')
word = list(strafe)
d_str = [i * 2 for i in word]
sym = [i + symbol for i in d_str]

print(d_str,sym)