roller = []
size = []
kon = int(input('кол во коньков'))
human = int(input('кол во людей'))
right = 0
for i in range(kon):
    razmer = int(input('введите размеры коньков'))
    roller.append(razmer)
for num in range(human):
    people = int(input('размер ноги'))
    size.append(people)
for number in size:
    for num in roller:
        if number <= num:
            right += 1
            roller.remove(num)
            break
print('кол во людей с роликами',right)
