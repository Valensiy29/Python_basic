strange = input('введите строку')
count = 0
simbol = set(".,;:!?")

for i_sim in strange:
    if i_sim in simbol:
        count += 1
print(count)