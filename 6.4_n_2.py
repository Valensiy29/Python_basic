import random

nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]

nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]

set_1 = set(nums_1)
set_2 = set(nums_2)

set_2.discard(min(set_2))
set_1.discard(min(set_1))

set_1.add(random.randint(100,200))
set_2.add(random.randint(100,200))

set_1.intersection(set_2)
set_1.difference_update(set_2)
