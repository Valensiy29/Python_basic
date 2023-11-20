text = input('введите текст').split()
word = input('введите искомые слова').split()

count = 0

for i in text:
    for num in word:
        if i == num:
            count += 1
print(count)