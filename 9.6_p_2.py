def remove_zen(zen):
    zen_remove = []
    for i in zen:
        zen_remove.append(i)
    zen_remove.reverse()
    print(''.join(zen_remove))
    zen.close()

zen = open('zen.txt', 'r')
remove_zen(zen)