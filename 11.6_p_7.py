import random


class People():


    def __init__(self,hungry,house,eat,money,name):
        self.name = name
        self.hungry = hungry
        self.house=house
        self.eat = eat
        self.money = money

    def select(self):
        self.cube_random = random.randint(1, 6)
        if self.hungry < 20 and self.eat > 10:
            self.hungry += 25
            self.eat -= 15
        elif self.eat < 10 and self.money > 50:
            self.eat += 30
            self.money -= 20
        elif self.money < 50:
            self.money += 30
        elif self.cube_random == 1:
            self.money += 20
        elif self.cube_random == 2:
            self.hungry += 15
        else:
            self.hungry -= 5
    def dead(self):
        if self.hungry < 0:
            print('хаги ваги он сгорел почернел')
        else:
            print('')
    def info(self):
        print('',self.hungry,'\n',self.house,'\n',self.eat,'\n',self.money,'\n',self.cube_random)


player_1 = People(50,True,50,200,'Pisya')
player_2 = People(50,True,50,200,'Popa')
counter = 365
while counter > 1:
    counter -= 1
    print('1 игрок')
    player_1.select()
    player_1.info()
    player_1.dead()
    print('2 игрок')
    player_2.select()
    player_2.info()
    player_2.dead()


