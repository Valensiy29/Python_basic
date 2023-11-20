class Parent:
    name = 'Mom'
    age = 10
    list_child = ['Tom','Penis']
    def info_mom(self):
        print(self.age,self.name,self.list_child)
    def pretty_child(self):
        if Child.angry:
            Child.angry = False
        elif Child.hungry:
            Child.hungry = False
class Child:
    name = 'Penis'
    age = 45
    angry = True
    hungry = True