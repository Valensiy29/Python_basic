spisochek = ['Artem','Boris','Vlad','Gosha','Dima','Evgesha','Zhenya','Zaxar']
new_spis = []
number_1 = 0
for i,number in enumerate(spisochek):
    if i == number_1:
        new_spis.append(number)
        number_1 += 2
print(new_spis)