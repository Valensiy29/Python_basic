def do_more(num):
        def repeat(func):
            def wrapped(*args,**kwargs):
                for _ in range(num):
                    res = func(*args,**kwargs)
                return
            return wrapped
        return repeat




@do_more(num=2)
def a():
    print('a')


a()