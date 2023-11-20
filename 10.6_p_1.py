def name_len(file):
    counter = 0
    line = 0
    for i in file:
        line += 1
        if len(i) <= 3:
            print('хуева')
            raise ('Ошибка: менее трёх символов в строке', line)
        else:
            counter += len(i) - 1
    return counter


file = open('people.txt','r',encoding = 'utf8')
name_len(file)