class Person:
    __name = 'Valya'
    __last_name = 'Davydov'
    __age = 13
class Employee:
    def work_money(self):
        self.money = 0

class Manager(Employee):
    def work_money(self):
        self.money = 13000
        return self.money


class Agent(Employee):
    def __init__(self,sell):
        self.sell = sell
    def work_money(self):
        self.money = 5000 + (self.sell / 100 * 5)
        return self.money


class Worker(Employee):
    def __init__(self,work_hours):
        self.work_hours = work_hours
    def work_money(self):
        self.money = self.work_hours * 100
        return self.money


corporetion = ['worker','worker','worker','agent','agent','agent','manager','manager','manager',]

work_1 = Worker(100)
work_2 = Agent(100)
work_3 = Manager()

for i in corporetion:
    if i == 'worker':
        print(work_1.work_money())
    elif i == 'agent':
        print(work_2.work_money())
    elif i == 'manager':
        print(work_3.work_money())