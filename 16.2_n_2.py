from contextlib import contextmanager
import os


@contextmanager
def in_dir(travel):
    cur_path = os.getcwd()
    os.chdir(travel)
    try:
        yield
    finally:
        os.chdir(cur_path)


with in_dir('C:\\'):
    print(os.listdir())