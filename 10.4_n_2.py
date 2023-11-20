file_word = open('word_2.txt', 'r', encoding='utf8')
file_error = open('error.log','r')

num = [1,2,3,4,5,6,7,8,9,0,'\n']
counter = 0

try:
    for i in file_word:
        pali = [word for word in i if word not in num]
        result = list(reversed(pali))
        if result == pali:
            counter += 1
        elif i in num and i != '\n':
            raise ValueError ('z ndjq hjn hf[fk')

except (ValueError) as error:
    file_error.write(error)
    raise ('я старался')
else:
    print(counter)
finally:
    file_error.close()
    file_word.close()