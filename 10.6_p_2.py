import random
number = random.randint(0, 100)
file_2 = open('result.txt', 'w')
file = open('coordinates.txt', 'r')

def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y

def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x

try:
    for line in file:
        nums_list = line.split()
        res1 = f(int(nums_list[0]), int(nums_list[1]))
        res2 = f2(int(nums_list[0]), int(nums_list[1]))
        my_list = sorted([res1, res2, number])
        file_2.write(' '.join(my_list))

except:
    print('что то не так')


finally:
    file.close()
    file_2.close()

