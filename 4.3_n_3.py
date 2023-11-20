import random

fr_list = [random.randint(50,80) for i in range(10)]
sec_list = [random.randint(30,60) for i in range(10)]

new_list = ['выжил' if fr_list[i] + sec_list[i] < 100 else 'погиб' for i in range(10)]
print(new_list)
print(fr_list,sec_list)