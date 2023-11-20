class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age
    @property
    def get_age(self):
        return self._age
    @property
    def get_name(self):
        return self._name

    def __repr__(self):
        return f"({self._name}, {self._age})"




first = Person("Max", 29)
second = Person("Christine", 21)
third = Person("Anthony", 35)

people = [first, second, third]

people.sort(key=lambda x: x._age)
print(people)