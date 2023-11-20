class Dot:
    count = 0
    def __init__(self,x=0,y=0):
        Dot.count += 1
        self.x = x
        self.y = y
        print(Dot.count)
    def info(self):
        print(self.x,self.y)

dot_1 = Dot(1,2)
dot_1.info()
