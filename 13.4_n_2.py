import random


class Iterators:
    start = 0
    elems = random.uniform(0.1,1.0)
    def __init__(self,elem):

        self.elem = elem
    def __iter__(self):
        return self
    def __next__(self):
        self.start += 1
        if self.start - 1 >= self.elem:
            raise ('SIuuuuuuuu')
        Iterators.elems += random.uniform(0.1,1.0)
        return Iterators.elems



iter = Iterators(6)
for i_elem in iter:
    print(i_elem)