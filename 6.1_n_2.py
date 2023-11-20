inof = input('Введите информацию о студенте через пробел (имя, фамилия, город, место учёбы, оценки):')
inf = inof.split()
information = dict()

information['Имя'] = inf[0]
information['Фамилия'] = inf[1]
information['город'] = inf[2]
information['место учебы'] = inf[3]
information['оценки'] = []

for i in inf[4:]:
    information['оценки'].append(i)
print(information)
