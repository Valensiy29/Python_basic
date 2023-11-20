def slicer(rand_num,slice):
    sli_tup = [slice[rand_num:]]
    for i,index_1 in enumerate(sli_tup):
        for num,index_2 in enumerate(sli_tup):
            if i == num:
                good = sli_tup[index_1:index_2]
                return good



rand_num = int(input('введите случайное число'))
slice = (1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10)
print(slicer(rand_num,slice))