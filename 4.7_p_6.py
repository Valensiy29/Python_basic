import random

count = int(input('кол-во чисел в списке'))

random_num = [random.randint(0,2)for _ in range(count)]
print('список до ',random_num)
for i in random_num:
    if i == 0:
        random_num.remove(i)
print('список после',random_num)
