class Robot:
    def __init__(self,model):
        self.model = model
    def operate(self):
        print('я робот')


class Can_Fly:
    def __init__(self,high,speed):
        self.high = high
        self.speed = speed
    def fly(self):
        self.high += 1
    def speed(self):
        self.speed += 1
    def on_earth(self):
        self.high = 0


class Dron(Robot,Can_Fly):
    def __init__(self,model,pos):
        super().__init__(model=model)
        self.pos = pos
    def operate(self):
        print('веду разведку с воздуха')
        self.pos += 1

class War_Robot(Robot,Can_Fly):
    def __init__(self,gun,model):
        super().__init__(model=model)
        self.gun = gun
    def operate(self):
        print('защещаю тереториc c помощью ', self.gun)


my_robot = Dron(0,0)
my_robot_2 = War_Robot('ананас','')

print(my_robot_2.operate(),my_robot.operate())
