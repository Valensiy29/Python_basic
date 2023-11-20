class Figure:
    def __init__(self,x,y,lenght,size):
        self.x = x
        self.y = y
        self.lenght = lenght
        self.size = size

    def move(self):
        self.x += 1
        self.y += 1

    def __str__(self):
        return self.x,self.y,self.lenght,self.size

class FigureMixin:
    def resize(self,lenght,size):
        self.lenght = lenght
        self.size = size

class NotSquare(Figure,FigureMixin):
    pass

class Square(Figure,FigureMixin):
    def __init__(self, pos_x, pos_y, size_2):
        super().__init__(pos_x, pos_y, size_2, size_2)


    # def resize(self,lenght,size):
    #     if self.lenght != self.size:
    #         print('у квадрата все стороны равны')
    #     else:
    #         self.lenght = lenght
    #         self.size = size

