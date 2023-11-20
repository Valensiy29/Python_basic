file = None
result = None

try:
    file = open('ages.txt','r')
    result = open('result.txt', 'x')

except (FileExistsError, PermissionError) as exc:  # названия исключений можно группировать в кортежи
    print("Поймано исключение: ", exc, type(exc))


if file and result:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    count = 0
    for i in file:
        try:
            result.write(alphabet[count] + '-' + i + '\n')
            count += 1
        except (ValueError, TypeError) as exc:
            print("Поймано исключение: ", exc, type(exc))