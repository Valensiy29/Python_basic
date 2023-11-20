mem = []

num = 1
members = int(input('сколько участников: '))
half = int(input('введите делитель: '))

for i in range(members // half):
    if members % half == 0:
        mem.append(list(range(num,num + half)))
        num += half
    else:
        print('запледеся жопой помидора')
print(mem)