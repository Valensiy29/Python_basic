class Family:
    name = 'Petrovyi'
    money = 100
    have_house = False

    def info(self):
        print('имя',self.name,'\n','money',self.money,'\n','house',self.have_house,'\n')

    def farm_money(self,gived_money):

        self.money += gived_money
        print('как скажешь')

    def duy_house(self,price_house,sale = 0):
        if not self.have_house:
            if self.money >= price_house - sale:
                self.have_house = True
                print('Покупка прошла успешно')
            else:
                quest = input('не хватает денег добавить?')
                if quest.lower() == 'да':
                    how_m = int(input())
                    self.money += how_m
                    self.duy_house(price_house,sale = 0)
                print('ок')
        else:
            print('все плоха')

fam = Family()

gived_money = int(input('дай деньги'))
price_house = int(input('сколько дом стоит'))
sale = input('будет скидка')
if sale.lower() == 'да':
    sale_1 = int(input())

fam.info()
fam.farm_money(gived_money)
fam.duy_house(price_house,sale_1)