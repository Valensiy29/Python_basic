class Human:
    count = 0
    def __init__(self,age,name):
        self.__name = 'Tom'
        self.__age = 34
        self.set_age(age)
        self.set_name(name)
        Human.count += 1
    def set_age(self,age):
        if self.__age in range(0,100):
            return self.__age
        else:
            raise ValueError
    def get_age(self):
        return self.__age
    def set_name(self,name):
        if str(self.__name):
            return self.__name
        else:
            raise TypeError
    def get_name(self):
        return self.__name