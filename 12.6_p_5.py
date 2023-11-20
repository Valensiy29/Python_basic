

class Car:
    def __init__(self,x,y,way,travel):
        self.x = x
        self.y = y
        self.travel = travel
        self.way = way
    def other_travel(self):
        for i in range(int(len(self.travel))):
            self.travel -= 1
            self.x += 1
            if float(self.way):
                self.y += 1
            if self.travel == 0:
                print('путь пройден')
                break
        self.other = input('введите координаты нового направления')
class Autobus(Car):
    passagers = 5
    money = 0
    def input(self):
        self.passagers += 1
    def other_travel(self):
        while True:
            for i in range(int(self.travel)):
                self.travel -= 1
                self.money += 100
                self.passagers -= 1
                if self.travel == 0:
                    print('путь пройден')
                    break
            self.travel = int(input('введите координаты нового направления'))
    def info(self):
        print(self.money,self.passagers,self.travel)


bus_station = Autobus(1,1,1.5,15)
print(bus_station.other_travel(),bus_station.info())