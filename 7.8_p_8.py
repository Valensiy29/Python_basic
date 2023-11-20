phone_book = dict()
while True:
    print('Введите номер действия: ','\n','1 - добавить контакт ','\n','2 - найти человека')
    choose = int(input('введите номер действия'))
    if choose == 1:
        names = input('Введите имя и фамилию нового контакта (через пробел):').split()
        name = tuple(names)
        mobile = int(input('введите номер телефона'))
        phone_book[name] = mobile
        print('Текущий словарь контактов: ', phone_book)
    elif choose == 2:
        l_n = input('введите фамилию для поиска')
        for i_n,i_num in phone_book.items():
            if l_n in i_n:
                print(i_n,i_num)

