def num_count(str_2):
    number = 0
    new = []
    for i in strafe:
        for num in str_2:
            if i == num:
                new.append(i)
                number += 1

    print(strafe)
    return number


strafe = input('введите строку')
str_2 = list(strafe)

num_count(str_2)