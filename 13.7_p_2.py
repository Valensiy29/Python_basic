import os


def gen_files_path():
    directory = os.path.abspath('Home_work')
    for i in os.walk(directory):
        print(i)

gen_files_path()