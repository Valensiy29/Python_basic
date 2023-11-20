def num_count(num):
    print(num)
    if num <= 1:
        return 1
    return num_count(num-1)
def nu():
    return num_count(num)

num = int(input('Введите num:'))
nu()