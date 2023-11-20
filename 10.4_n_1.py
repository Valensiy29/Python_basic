file_name = open('words.txt','r',encoding='utf8')
counter = 0
for i in file_name:
    print(i)
    if len(i) - 1  < 3:
        print(counter)
        raise TypeError ('ты еблан?')
    counter += len(i)

print(counter)