sher_1 = list(range(160,176,2))
sher_2 = list(range(162,180,3))
sher_1.extend(sher_2)
for i in range(len(sher_1)):
    for num in range(i,len(sher_1)):
        if sher_1[i] > sher_1[num]:
            sher_1[i],sher_1[num] = sher_1[num],sher_1[i]

print(sher_1)