import os


class File:
    def __init__(self,name,work):
        self.name = name
        self.work = work

    def __enter__(self):
        if not os.path.exists(self.name):
            return open(self.name,'w')
        return open(self.name,self.work)

    def __exit__(self, exc_type, exc_val, exc_tb):
        file.close()
        return True


with File('e.txt', 'r') as file:
    file.write('Всем привет!')