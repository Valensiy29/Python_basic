import os
import random

def find_file(cur_path, file_name):
    all_paths = []
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if file_name == i_elem:
            all_paths.append(os.path.abspath(path))
        elif os.path.isdir(path):
            result = find_file(path, file_name)
            if result:
                all_paths.extend(result)

    return all_paths


def check_file_inside(path_to_file):
    file = open(path_to_file, 'r', encoding='utf8')
    for line in file:
        print(line)
    file.close()


all_paths = find_file('../..', '9.3_n_2.py')
check_file_inside(random.choice(all_paths))