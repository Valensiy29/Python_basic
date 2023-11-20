class Planet:
    cast = {'Вода + Воздух':'Шторм','Вода + Огонь':'Пар',
            'Вода + Земля':'Грязь','Воздух + Огонь':'Молния','Воздух + Земля':'Пыль','Огонь + Земля':'Лава'}
    def __add__(self, other):
        try:
            print(self.cast[other])
        except:
            print('None')


lif = Planet()
lif.__add__('Воздух')

