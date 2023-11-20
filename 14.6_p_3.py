import datetime
from typing import Callable


def logging(func: Callable) -> Callable:
    try:
        def wrapped_func(*args,**kwargs):
            print(func.__name__,func.__doc__)
            res = func(*args,**kwargs)
            return res
        return wrapped_func
    except:
        with open('function_errors.log ', 'w') as file:
            file.write(func.__name__)
            file.write(datetime.time)

@logging
def phone_book():
    phon_book = dict()
    name = input('введите имя')
    surname = input('введите фамилию')
    mod_phon = int(input('введите номер телефона'))
    if name not in phon_book:
        phon_book[name, surname] = mod_phon
    elif name in phon_book:
        print('человек уде есть в книжке')
    print(phon_book)

phone_book()