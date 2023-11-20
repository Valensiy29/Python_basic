

with open('calc.txt', 'r') as file:
    result = 0
    print('содержимое файла')
    for i in file:
        print(i)
        arifmetic = i.split()
        if arifmetic[1] == '/':
            result += int(arifmetic[0]) / int(arifmetic[2])
        elif arifmetic[1] == '*':
            result += int(arifmetic[0]) * int(arifmetic[2])
        elif arifmetic[1] == '-':
            result += int(arifmetic[0]) - int(arifmetic[2])
        elif arifmetic[1] == '+':
            result += int(arifmetic[0]) + int(arifmetic[2])
        elif arifmetic[1] == '%':
            result += int(arifmetic[0]) % int(arifmetic[2])
        else:
            question = input('Обнаружена ошибка в строке: ' + i + ' Хотите исправить?').lower()
            if question == 'да':
                arifmetic = input('Введите исправленную строку: ').split()
                if arifmetic[1] == '/':
                    result += int(arifmetic[0]) / int(arifmetic[2])
                elif arifmetic[1] == '*':
                    result += int(arifmetic[0]) * int(arifmetic[2])
                elif arifmetic[1] == '-':
                    result += int(arifmetic[0]) - int(arifmetic[2])
                elif arifmetic[1] == '+':
                    result += int(arifmetic[0]) + int(arifmetic[2])
                elif arifmetic[1] == '%':
                    result += int(arifmetic[0]) % int(arifmetic[2])

print('Сумма результатов: ',result)
