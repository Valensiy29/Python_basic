strafe = input('введите строку')
print(list(filter(lambda x: not (x.isupper() or x.isdigit()),strafe)))