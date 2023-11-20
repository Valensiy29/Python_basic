def chipher(file,chipher_file):

    line_num = 0
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in file:
        res_chipher = ''
        line_num += 1
        word_sph = []
        for line in i.lower():
            if line in alphabet:
                word_sph.append(line)
                sum = alphabet.index(line) + line_num
                res_chipher += alphabet[sum]
        chipher_file.write(res_chipher)
        chipher_file.write('\n')
        print(res_chipher)

file = open('text.txt','r',encoding='utf8')
chipher_file = open('chipher_text.txt','a')
chipher(file,chipher_file)