students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}




def function(dict):
    pairs = {}
    lst = []
    string = ''
    cnt = 0
    for i in dict:
        lst += dict[i]['interests']
        string += dict[i]['surname']
    for _ in string:
        cnt += 1
    for i in students:
        pairs[i] = (students[i]['age'])
    return lst, cnt, pairs







my_lst = function(students)[0]
len = function(students)[1]
pairs = function(students)[2]

print('Полный список интересов всех студентов:',my_lst,'\n','Общая длина всех фамилий студентов: ',len,'\n',
      'Список пар "ID студента — возраст":', pairs)