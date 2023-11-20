index_list = []
count = int(input('введите колдичество чисел: '))
for numbers in range(count):
    del_num = int(input('введите число:'))
    index_list.append(del_num)
deleter = int(input('введите делитель:'))
index = 0
sum_in = 0
for num in index_list:
    if num % deleter == 0:
        print('индекс числа:',num,',',index)
        sum_in += index
    index += 1
print('сумма индексов: ',sum_in)
