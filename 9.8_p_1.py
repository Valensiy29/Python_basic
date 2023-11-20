def sum_of_num(file):
    count_num = 0
    for i in file:
        for x in i.split():
            count_num += int(x)
    file.close()
    return count_num

file = open('numbers.txt', 'r')
sum_of_num(file)
