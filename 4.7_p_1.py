conect = ['а','у','о','ы','э','я','ю','ё','и','е']

new_spis = []

text = input('введите текст')
word = list(text)

for num in conect:
    for i in word:
        if num == i:
            new_spis.append(i)
print(new_spis)
print(len(new_spis))
