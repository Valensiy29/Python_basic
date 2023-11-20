def min_num_2(number):
    for num in range(number):
        ex = True
        number_2 = 0
        num = 2
        number_2 += number / num
        try:
            int(number_2)
            return ex
        except ValueError:
            num += 1
            return False


#def min_num(number):
    #trFl = min_num_2(number)
    #if trFl == True:



number = int(input('введите число: '))
min_num_2(number)

