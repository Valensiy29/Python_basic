class Can_Fly:
    def __init__(self,high,speed):
        self.high = high
        self.speed = speed
    def fly_up(self):
        pass
    def flying(self):
        pass
    def fly_down(self):
        self.high = 0
        self.speed = 0
    def info(self):
        print(self.speed,self.high)


class Battefly(Can_Fly):
    def fly_up(self):
        self.high = 1
    def flying(self):
        self.speed = 0.5

class Rocket(Can_Fly):
    def fly_up(self):
        self.high = 500
    def flying(self):
        self.speed = 1000
    def fly_down(self):
        self.high = 0
        print('пиздос')

        
but = Battefly(1,1)
roc = Rocket(2,2)

print(but.fly_up(),but.fly_down(),but.flying())

print(roc.fly_up(),roc.fly_down(),roc.flying())