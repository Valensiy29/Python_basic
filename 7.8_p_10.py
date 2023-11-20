def shorter_object(strafe,tup_num):
    return min(len(strafe),len(tup_num))



strafe = input('Строка: ')
tup_num = input('Кортеж чисел: ')

pairs = ((strafe[i_elem],tup_num[i_elem])
         for i_elem in range(shorter_object(strafe,tup_num)))

for i in pairs:
    print(i)

print(pairs)
