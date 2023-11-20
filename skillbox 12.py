def greeting():
    print('Привет!')
    print('Добро пожаловать!')


while True:
    a = input('Зайдёте? Да/Нет: ')
    if a == 'Да':
        greeting()
    print('Следующий.\n')


def food():
    print("Сколько мешков рыбы и мяса?")
    a = int(input())
    b = int(input())
    print("Всего", a + b, "шт.")


print("Сколько буханок белого и чёрного хлеба?")
food()
print("Сколько вёдер воды и молока?")
food()


def place():
    lastname = input('Фамилия')
    name = input('Имя')
    street = input('улица')
    house = int(input('дом'))


print()
place()
print()
place()
print()
place()


def aboutWater(stoim):
    print('Название: КлирВотер'
          '\nПроизводитель: ВодЗавод'
          '\nцена: ', stoim)


chena = int(input("введите цену"))
print()
aboutWater(chena)
print()
aboutWater(chena)
print()
aboutWater(chena)

import math


def sphereArea():
    planet = float(input('Введите размерыы планеты: '))
    planet = 4 * math.pi * planet ** planet
    print(planet)


def sphereVolum():
    planet = float(input('Введите размерыы планеты: '))
    planet = (4 / 3) * math.pi * planet ** 3
    print(planet)


print()
sphereArea()
print()
sphereVolum()


def isPrime(n):
    for chisla in range(2, int(n ** .5)):
        if n % chisla == 0:
            print('НЕ ПРОСТОЕ')
    else:
        print('prostoe')


number = int(input('chislo vvodi'))
for i in range(number):
    new_number = int(input("Введите число: "))
    isPrime(new_number)


def mediumAref():
    sred = (x + y) / 2
    print(sred)


x = float(input('введите левую границу'))
y = float(input('введитье правую границу'))
mediumAref()


def pasport(surname, name, country, city, street, house, flat):
    print(f"Фамилия: {surname}\n"
          f"Имя: {name}\n"
          f"Страна проживания: {country}\n"
          f"Город: {city}\n"
          f"Улица: {street}\n"
          f"Номер дома: {house}\n"
          f"Номер квартиры: {flat}")


for number in range(3):
    user_surname = input("Введите фамилию: ")
    user_name = input("Введите имя: ")
    user_country = input("Введите страну проживания: ")
    user_city = input("Введите город: ")
    user_street = input("Введите улицу: ")
    user_house = input("Введите номер дома: ")
    user_flat = input("Введите номер квартиры: ")
    pasport(user_surname, user_name, user_country, user_city, user_street, user_house, user_flat)
import math


def my_distance(x, y):
    distance = math.sqrt(x ** 2 + y ** 2)
    print(distance)


def their_distance(x_1, x_2, y_1, y_2):
    distance = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
    print(distance)


question = input('1 - от меня до точки, 2 - от точки до точки: ')
if question == 1:
    x = int(input('введите координаты первой точки'))
    y = int(input('введите координаты второй точки'))
    my_distance(x, y)
elif question == 2:
    target_x_1 = float(input("Введите координату X цели 1: "))
    target_y_1 = float(input("Введите координату Y цели 1: "))
    target_x_2 = float(input("Введите координату X цели 2: "))
    target_y_2 = float(input("Введите координату Y цели 2: "))
    their_distance(target_x_1, target_x_2, target_y_1, target_y_2)


def summa_n(chifirka):
    for number in range(chifirka + 1):
        number += chifirka + number
    print('я знаю что сумма чисел от 1 до ',chifirka,' равна ', number)


chifirka_2 = int(input('Введите число: '))
summa_n(chifirka_2)


def test(tester):
    def positive():
        print('Положительное')
    if tester > 0:
        positive()
    def negative():
        print('отрицательное')
    if tester < 0:
        negative()
tester = float(input('введите число: '))
test(tester)

def count_letters(text):
    total_num = 0
    total_word = 0
    if number == num:
        total_num += 1
        print(total_num)
    elif numb == word:
        total_word += 1
        print(total_word)
text_2 = input('введите текст')
num = int(input('какую chifru ищем'))
word = input('какую цифру ищем')
for number in text_2:
    count_letters(text_2)
for numb in text_2:
    count_letters(text_2)

def plus(num):
    total_num = 0
    for number in range(0,num):
        total_num = number + number
        print(total_num)

num = int(input('введите число: '))
queston = int(input('1-max,2-minimal,3-plus: '))
if queston == 1:
    plus(num)



def count_letters(word,num,text_2):
    t_word = 1
    t_num = 1
    for number in text_2:
        if num == number:
            t_num += 1
    print(t_num+1)
    for numb in text_2:
        if word == numb:
            t_word += 1
    print(t_word+1)

text_2 = input('введите текст')
word = input('какую bukvu ищем')
num = int(input('какую chifru ищем'))
total_word = 1
total_num = 1
count_letters(word,num,text_2)

