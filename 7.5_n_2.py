
phon_book = dict()

while True:
    name = input('введите имя')
    surname = input('введите фамилию')
    mod_phon = int(input('введите номер телефона'))
    if name not in phon_book:
        phon_book[name, surname] = mod_phon
    elif name in phon_book:
        print('человек уде есть в книжке')
    print(phon_book)
    if name == 'popa':
        break