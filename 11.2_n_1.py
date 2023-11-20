class Toyota:
    colr_of_car = 'white'
    price = 1000000
    speed_now = 0
    max_speed = 220
    def info(self):
        print(self.colr_of_car,self.price,self.speed_now,self.max_speed)
    def __init__(self,colr_of_car = 'white',price = 1000000,speed_now = 0,max_speed = 220):
        self.colr_of_car = colr_of_car
        self.price = price
        self.speed_now = speed_now
        self.max_speed = max_speed


car = Toyota()
car.info()

