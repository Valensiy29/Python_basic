friend = int(input('сколько друзей'))
credit = int(input('Долговых расписок'))
creditor = []
for i in range(friend):
    creditor.append(0)
for num in range(credit):
    print(num,'расписка')
    who = int(input('кому'))
    f_him = int(input('От кого'))
    much = int(input('сколько'))
    creditor[who - 1] -= much
    creditor[f_him - 1] += much
for i in range(friend):
    print(i +  1,':',creditor[i])

