def numbers(number):
    spisok = []
    for i in range(1,number+1,2):
        spisok.append(i)
    print(spisok)

number = int(input('введите число: '))
numbers(number)