import os

def find_object(directory,file):
    for i_elem in os.listdir(directory):
        path = os.path.join(directory,i_elem)
        if file == i_elem:
            print('путь до файла',os.path.abspath(os.path.join(i_elem)))
        elif os.path.isdir(path):
            result = find_object(path,file)
            if result:
                break
        file_1 = open(path,'r',encoding = 'utf = 8')

        




way = find_object('..', '9.2_n_1.py')

