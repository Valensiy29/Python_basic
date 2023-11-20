class Circel:

    def __init__(self, x = 0 ,y = 0 ,r = 1, k = 0):
        self.__x = x
        self.__y = y
        self.r = r
        self.k = k
    def circel_s(self,r):
        result = 0
        result += 3.14 * (r ** 2)
        return result

    def circel_c(self,r):
        res = 0
        res += 2 * 3.14 * r
        return res

    def circel_k(self,k,r):
        ke = 0
        ke += k * r
        return ke
    def __str__(self):
        return self.__x,self.__y
    def get_x(self):
        return self.__x
    def set_x(self):
        if int(self.__x):
            return self.__x
        else:
            raise ('Нахуй пошел')
    def get_y(self):
        return self.__y
    def set_y(self):
        if int(self.__y):
            return self.__y
        else:
            raise ('Нахуй пошел')


circel_1 = Circel(1,1,1)
circel_2 = Circel(1,1,2)

