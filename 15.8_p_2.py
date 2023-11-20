class MyMath:
    def circle_len(self,r):
        return (2 * 3.14) * r
    def s_circle(self,r):
        return 3.14 * (r ** 2)
    def square_v(self,a,b,c):
        return a * b * c
    def sphere_s(self,r):
        return 4 * 3.14 * r ** 2

res_1 = MyMath().circle_len(r=5)
res_2 = MyMath().sphere_s(r=6)
print(res_1)
print(res_2)