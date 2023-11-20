want = int(input('введите кол-во заказов'))
print('«Покупатель — название пиццы — количество заказанных пицц»')
knows = dict()
knows_2 = dict()

for i in range(want):
    choose = input('введите заказ:').split()
    knows_2[choose[1]] = choose[2]
    knows[choose[0]] = knows_2
