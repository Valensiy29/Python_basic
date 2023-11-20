import os


def gen_files_path():
    counter = 0
    directory = os.path.abspath('..')

    for i in os.listdir(directory):
        print(i)
        file = open(i,'r')
        for _ in file:
            counter += 1
    yield counter

for i in gen_files_path():
    print(i)