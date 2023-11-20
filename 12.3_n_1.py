class Ship:
    def __init__(self,model):
        self.model = model
    def move(self):
        print('корабль двигается')
    def __str__(self):
        return self.model
class CargoShip(Ship):
    def __init__(self,model,carg):
        super().__init__(model)
        self.carg = carg
        self.model = 'cargo'
    def uncargo(self):
        print('корабль разгружен')
        self.carg = 0
class WarShip(Ship):
    def attack(self):
        print('атакую')
    def __init__(self,model,weapon):
        super().__init__(model)
        self.model = 'warship'
        self.weapon = weapon