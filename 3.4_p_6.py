three_num = []
sev_num = []
for i in range(3):
    num = int(input('введите числло'))
    three_num.append(num)
for i in range(7):
    num = int(input('введите числло'))
    sev_num.append(num)

for i in three_num:
    for num in sev_num:
        while num != i:
            print('')
            break
    sev_num.remove(sev_num.count(i))
    #sev_num.extend(three_num)
print(sev_num)
