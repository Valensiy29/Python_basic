import random


class Carma:
    constant = 0
    def get_one_day(self):
        while True:
            rand = random.randint(1,10)
            if rand == 1:
                with open('carma.log','w') as self.file:
                    print('рандомайзер смерти',rand)
                    self.file.write('KillError')
                    raise 'KillError'
            elif self.constant <= 500:
                self.constant += random.randint(1,7)
            elif self.constant >= 500:
                return self.constant

res = Carma()
print(res.get_one_day())