


class Player:
    def __init__(self,dot,name):
        self.dot = dot
        self.name = name

class Cell:
    def __init__(self):
        self.cell = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False}
    def step(self):
        self.point = Player
        if self.cell[point] == False:
            self.cell[point] = True
        else:
            print('занято')
# class Board:
#     res = Cell
#     print()
#     print(' ___________________','\n','|__',res.cell[point],'__|__',,'__|__',,'__|'''
#      ,' ___________________','\n','|__',,'__|__',,'__|__',,'__|'''
#      ,' ___________________','\n','|__',,'__|__',,'__|__',,'__|'''.format())

point = int(input('введите точку хода'))
player_1 = Player(point,'dot')
player_2 = Player(point,'')
print(Cell.step)

