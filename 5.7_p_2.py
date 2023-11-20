strafe = input('введите строку').split()
str_2 = strafe[:]

number = -1
fku = -1

for i in strafe:
    for num in str_2:
        if len(strafe[number]) < len(str_2[fku]):
            strafe.remove(num)
        else:
            fku += 1
    number += 1

print(strafe)