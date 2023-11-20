good_log = open('good_log.txt','w')
bad_log = open('bad_log.txt','w')

with open('registrations.txt', 'r', encoding='utf8') as file:
    for i in file:
        if len(i) - 1 < 3:
            raise IndexError
        log = i.split()
        for line in log:
            if '@' not in log[1] or '.' not in log[1]:
                bad_log.write(line)
                raise SyntaxError
            elif int(log[2]) > 99 or int(log[2]) < 10:
                bad_log.write(line)
                raise ValueError
            elif not str(log[0]):
                bad_log.write(line)
                raise NameError
            else:
                good_log.write(line)