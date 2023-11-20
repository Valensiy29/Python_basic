# fir = []
res = []

fir_let = input('Введите первое сообщение')
twe_let = input('введите второе сообщение')
fir_count = fir_let.count('!') + fir_let.count('?')
twe_count = twe_let.count('!') + twe_let.count('?')
word_1 = list(fir_let)
word_2 = list(twe_let)
if fir_count > twe_count:
    print(word_1.extend(word_2))
elif fir_count== twe_count:
    print('ой')
else:
    print(word_2.extend(word_1))







