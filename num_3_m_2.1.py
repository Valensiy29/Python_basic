work_num = int(input('сколько сотрудников в офисе'))
id = []  
for number in range(work_num):
    work_id = int(input('ID сотрудника'))
    id.append(work_id)

id_question = int(input('какой ID ищем'))
for work_id in id :
    if id_question == work_id:
        print('сотрудник работает')
        break
    else:
        print('Сотрудник не работает')
        break