stroka = input('введите строку')
set_st = set(stroka)
spis = []
for x in set_st:
    if '0'<=x<='9':
        spis.append(x)
print(spis)