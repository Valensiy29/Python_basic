count = int(input('кол во пар слов'))

alpha = dict()

chet = 0

for i in range(count):
    sinom = input('введите слова синонимы').split()
    for num,index in enumerate(sinom):
        alpha[sinom[0]] = sinom[1]
        alpha[sinom[1]] = sinom[0]
        chet += 1

#for num in range(count):
for i in alpha:
    choose = input('введите один из синонимов')
    if alpha.get(choose) not in alpha:
        print('error')
    print(alpha.get(choose))