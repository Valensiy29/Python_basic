def insane():
    while True:
        yield __iter__

def __iter__():
    num = 0
    while True:
        num += 1
        return num


for i in insane():
    print(i)