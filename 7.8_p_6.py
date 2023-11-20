sis = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tup = []

for i_in,i_num in enumerate(sis):
    if i_in % 2 == 0:
        new_sis = tuple(sis[i_in - 2:i_num])
        tup.append(new_sis)
print(tup)