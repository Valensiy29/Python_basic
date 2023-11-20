# for i in range(4):
#     ip = int(input('введите число'))
#     address = '{0}.'.format(ip)
# print(address)

ip_address = "{0}.{1}.{2}.{3}"
count = 0
numbers = []
while count < 4:
    new_number = int(input("Введите число: "))
    numbers.append(new_number)
    if 0 <= new_number <= 255:
        count += 1

print(ip_address.format(*numbers))
# * полезный инструмент, но и без него можно справиться, вручную прописав элементы по индексам
print(ip_address.format(numbers[0], numbers[1], numbers[2], numbers[3]))