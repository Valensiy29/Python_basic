def finobachi(pos_num):
    fin = [1,1]
    for i,index in enumerate(fin):
        res = fin[i + 1] + fin[i]
        fin.append(res)
        if i + 2 == pos_num:
            return fin[pos_num]

pos_num = int(input('Введите позицию числа в ряде Фибоначчи: '))
finobachi(pos_num)