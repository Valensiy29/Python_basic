import random

max_n = int(input('введите максимальное число'))
rand = [random.randint(0,max_n) for _ in range(3)]
ask = []

while True:
    question = input('нужное число есть среди этих чисел?')

    if question == 'Помогите!' or question == 'помогите!':
        print('Я загадал эти числа',rand)
        break
    for num in rand:
        for i in ask:
            if num == i:
                print('да')
                break
            else:
                print('нет')
                break
    print(rand,question)