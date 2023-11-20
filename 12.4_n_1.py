class Unit:
    def __init__(self,health,damage):
        self.health = health
        self.damage = damage


class Soldier(Unit):
    def hit_point(self,health,damage):
        super().__init__(damage, health)
        health -= damage
    def get_health(self, health):
        return health


class Human(Unit):
    def hit_point(self,health,damage):
        super().__init__(damage,health)
        health -= damage * 2
    def get_health(self,health):
        return health

unit_1 = Soldier(20,100)
unit_2 = Human(20,100)

print(unit_1.hit_point(20,100))
print(unit_2.hit_point(20,100))
