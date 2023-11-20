


class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}'.format(
            self.index, Potato.states[self.state]))


class PotatoGarden:
    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает!')
        for potato in self.potatoes:
            potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка ещё не созрела!\n')
            return False  # такой return поможет получить информацию о зрелости картошки снаружи этого объекта
        else:
            print('Вся картошка созрела. Можно собирать!\n')
            return True

    def print_all_states(self):
        for potato in self.potatoes:
            potato.print_state()



class Garder:
    name = 'Pedik'
    plants = PotatoGarden(5)
    def collect(self,plants):
        if plants.are_all_ripe():
            for i in plants.potatoes:
                plants.potatoes.remove(i)
            print('я все собрал. Я молодец')
            print(plants.potatoes)



garden = PotatoGarden(5)
gar = Garder()
for _ in range(3):
    garden.grow_all()
garden.are_all_ripe()
gar.collect(garden)