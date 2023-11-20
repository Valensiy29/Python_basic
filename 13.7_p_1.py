def gen(n):
    for i in range(n):
        yield i ** 2

class Iterationner:


    def __init__(self,num):
        self.num = num
        self.start = 0
    def __iter__(self):
        self.nums = 0
        return self
    def __next__(self):
        self.start += 1
        if self.start >= self.num:
            raise ('')
        self.nums += self.start ** 2
        print(self.nums)



generation = gen(10)

generation_2 = Iterationner(10)
for num in generation_2:
    print(num)

for i in generation:
    print(i)