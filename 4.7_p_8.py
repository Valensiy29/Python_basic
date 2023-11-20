import random

count = int(input('кол во палок'))
snipe = int(input('кол во бросков'))

stick = [num for num in range(1,count + 1)]
new_spis = []

for i in range(1,snipe + 1):
    left_i = random.randint(1,10)
    right_i = random.randint(1,10)
    print('Бросок ',i,'сбиты палки с',left_i,'по',right_i)
    if left_i > right_i:
        result = stick[right_i:left_i]
        new_spis.extend(result)
    else:
        result = stick[left_i:right_i]
        new_spis.extend(result)
# for num in new_spis:
#     for i in new_spis:
#         if num == i:
#             new_spis.remove(i)

print(new_spis)
