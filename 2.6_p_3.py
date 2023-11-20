cells_count =[]
new_spis = []
question = int(input('сколько клеток'))

for _ in range(question):
    cells = int(input('введите эффективность клетки'))
    cells_count.append(cells)
    for i,number in enumerate(cells_count):
        if i > number:
            new_spis.append(number)

print(new_spis)