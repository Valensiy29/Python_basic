old_card_2 = []
old_card = []
new_card = []
schet = -1
schet_2 = -2
card_count = int(input('введите кол-во видеокарт'))
for num in range(card_count):
    m_card = int(input('введите видеокарту'))
    old_card_2.append(m_card)
    old_card.append(m_card)
for i in range(card_count):
    if old_card[schet] > old_card_2[schet_2]:
        new_card.append(old_card_2)
        schet -= 1
        schet_2 -= 1
    else:
        new_card.append(old_card)
        schet -= 1
        schet_2 -= 1
    print(new_card)
