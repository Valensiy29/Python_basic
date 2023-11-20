phone = dict()
while True:
    print('Текущие контакты на телефоне:')
    print(phone)
    name = input('введите имя')
    number = int(input('введите номер телефона'))
    phone[name] = number
    if name in phone:
        print('Ошибка: такое имя уже существует.')
    print(phone)