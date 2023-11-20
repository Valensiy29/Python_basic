

def counter(func):
    def wrapped_counter(*args,**kwargs):
        wrapped_counter.count += 1
        res = func(*args,**kwargs)
        print(wrapped_counter.count)
        return res
    wrapped_counter.count = 0

    return wrapped_counter

@counter
def a():
    print('a')


a()
a()
a()



