class Property:
    def __init__(self,worth,money):
        self.worth = worth
        self.money = money
    def credit(self):
        pass

class Apartament(Property):
    def credit(self):
        if self.money != self.worth:
            self.worth_2 = self.worth - self.money
            credit_num = self.worth_2 / 1000
            return credit_num
        else:
            credit_num_2 = self.worth / 1000
            return credit_num_2

class Car(Property):
    def credit(self):
        if self.money != self.worth:
            self.worth_2 = self.worth - self.money
            credit_num = self.worth_2 / 200
            return credit_num
        else:
            credit_num_2 = self.worth / 200
            return credit_num_2


class CountryHouse(Property):
    def credit(self):
        if self.money != self.worth:
            self.worth_2 = self.worth - self.money
            credit_num = self.worth_2 / 500
            return credit_num
        else:
            credit_num_2 = self.worth / 500
            return credit_num_2


cred_1 = Apartament(10000000,100)

cred_2 = Car(5000000,100)

cred_3 = CountryHouse(20000000,100)

print(cred_1.credit(),cred_2.credit(),cred_3.credit(),)


