shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
['педаль', 100], ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
detail = input('Название детали')
total = 0
num = 0
sum = 0

for i in shop:
    if shop[num][0] == detail:
        sum += shop[num][1]
        total += 1
    num += 1

print('кол-во деталей', total)
print('общая стоимость',sum)