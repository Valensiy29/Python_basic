s = input('введите строку')
words = list(s)
changed_c = 0
index = 0
for index,i in enumerate(words):
    index += 1
    if i ==':':
        words[index - 1] = ';'
        changed_c += 1
print(changed_c,words)
