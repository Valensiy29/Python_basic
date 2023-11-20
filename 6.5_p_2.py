count = int(input('кол во стран'))
country = dict()
for i in range(count):
    fst_country = input('страна').split()
    for num in range(4):
        country[fst_country[num]] = fst_country[0]
for _ in range(3):
    city = input('введите город')
    if country.get(city) in country:
        print('город',city,'расположен в стране',country.get(city))
    elif country.get(city) not in country:
        print('По городу',city,'данных нет')