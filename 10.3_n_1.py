strafe_user = input('введите строку')
file = open('user_text','w',encoding='utf8')

try:
    file.write(strafe_user)
except FileExistsError:
    print('файл не найден')
else:
    print('ол гут май френд')
finally:
    file.close()