import os

directory = 'Home_work'

for i_elem in os.listdir(directory):
    print(os.path.abspath(i_elem))