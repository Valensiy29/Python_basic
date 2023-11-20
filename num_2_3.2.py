pay = []
Range = int(input('кол-во сотрудников'))

for _ in range(Range):
    add = int(input('зарплата сотрудника'))
    pay.append(add)

for i,indexer in enumerate(pay):

    if indexer == 0:
        pay.remove(indexer)
print(max(pay))
print(min(pay))
print(pay)
print(len(pay))