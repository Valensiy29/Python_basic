a = []
a_2 = []
count = 1
list = input('введите слово')
for i in list:
    a.append(i)
    a_2.append(i)
for i in reversed(a_2):
    for rev in a:
        if i == rev:

            count += 1
count /=2

if count == len(a):
    print('слово является палиндромом',a)
else:
    print('слово не является палиндромом',a)