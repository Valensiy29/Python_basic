class File:
    def __init__(self,name,work):
        self.name = name
        self.work = work

    def __enter__(self):
        return open(self.name,self.work)

    def __exit__(self, exc_type, exc_val, exc_tb):
        file.close()


with File('example.txt', 'w') as file:
    file.write('Всем привет!')