guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
print('сейчас на вечеринке ',len(guests),'человек',guests)


while True:
    question = input('Гость пришел или ушел?')
    name = input('Имя гостя? ')
    while question != 'Пора спать':
        if question == 'Пора спать':
            print('Сосать раки')
            break
        elif question == 'пришел':

                for i in guests:
                    if len(guests) != 6:
                        guests.append(name)
                        break
                    else:
                        print('нету мест')
                        break
        elif question == 'ушел':
            for i in guests:
                if i == name:
                    guests.remove(name)
                    break
        else:
            print('ошибка ввода, попробуйте еще раз')
            print('сейчас на вечеринке ',len(guests),'человек:', guests)
            break



