global_count = []


def counter(func):
    def wrapped_counter(*args,**kwargs):
        global count
        wrapped_counter.count += 1
        res = func(*args,**kwargs)
        global_count.append(wrapped_counter.count)
        return wrapped_counter.count, global_count
    wrapped_counter.count = 0
    return wrapped_counter



@counter
def a():
    print('a')


a()
a()
a()
