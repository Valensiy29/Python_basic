class Circel:
    def __init__(self, x = 0 ,y = 0 ,r = 1, k = 0):
        self.x = x
        self.y = y
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

circel_1 = Circel(1,1,1)
circel_2 = Circel(1,1,2)
cir_1 = (circel_1.x + circel_1.r) * 2
cir_2 = (circel_2.x + circel_2.r) * 2
if cir_1 == circel_2.x + circel_2.r:
    print('meet circle!!!')
elif circel_1.x + circel_1.r == cir_2:
    print('meet circle!!!')
else:
    print('meet does not exist :(((')
