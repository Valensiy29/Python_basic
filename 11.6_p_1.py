import random


class Hero:
    health = 100


unit_1 = Hero()
unit_2 = Hero()

while unit_1.health > 1 or unit_2.health > 1:
    attack = random.randint(1,2)
    if attack == 1:
        unit_2.health -= 20
        print(unit_2.health, 'осталось здоровья после удара unit_1')
        if unit_2.health == 0:
            break
    else:
        unit_1.health -= 20
        print(unit_1.health, 'осталось здоровья после удара unit_2')
        if unit_1.health == 0:
            break

if unit_1.health > unit_2.health:
    print('unit_1 killed unit_2')
elif unit_1.health < unit_2.health:
    print('unit_2 killed unit_1')
