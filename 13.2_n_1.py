items = [i for i in range(10000)]
iterator = iter(items)
try:
    while iterator:
        print(next(iterator))
except:
    print()