def answer_to_people(question,count = 4,delete = 'Удалить файл?'):
    while True:
        print(question)
        answer = input('')
        if answer == 'да':
            print(delete)
            ask = input()
            if ask == 'да':
                break
            else:
                print(count)
        elif answer == 'нет':
            print()
        else:
            print('Неверный ввод. Пожалуйста, введите да или нет.')
            print(count)


answer_to_people('Вы действительно хотите выйти?')
answer_to_people('Удалить файл',delete= 'Уверен')
answer_to_people('Jgbcfnm j,jljr eybnfpf',delete='Иди нахуй заёбал')