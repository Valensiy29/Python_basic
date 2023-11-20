class Robots:
    def __init__(self,model):
        self.model = model
    def __str__(self):
        return self.model
    def operate(self):
        print('кружу')
class RobotCleaner(Robots):
    def __init__(self,model):
        super().__init__(model)
        self.model = 'cleaner'
        self.vaacum = 0
    def operate(self):
        print('чищю ',self.vaacum)
        if self.vaacum == 100:
            print('во гандоны')
class WarRobot(Robots):
    def operate(self):
        print('я был рожден ебашить')
    def __init__(self,model):
        super().__init__(model)
        self.model = 'warRobot'
class SubmarineRobot(Robots):
    def operate(self):
        print('я был рожден ебашить под водой')
    def __init__(self,model):
        super().__init__(model)
        self.model = 'warRobot'

