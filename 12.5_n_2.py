def big_file():
    nums = 0
    with open('numbers.txt', 'r') as file:
        for i in file:
            if i != ' ' and i != '\n':
                clear_line_sum = sum(map(int, i.rstrip().split()))
                yield clear_line_sum
summ =0
for i in big_file():
    summ += i
print(summ)