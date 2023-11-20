part = input('Введите шаблон поздравления, в шаблоне можно использовать конструкцию {people} и {age}:')
people = input('список людей через запятую:').split(',')
age = input('Возраст людей через пробел: ').split()

for i in range(len(people)):
    result = part.format(people = people[i],age = age[i])
    print(result)