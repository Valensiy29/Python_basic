file = input('Название файла')

if file.endswith('.txt''.docx'):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
if file.startswith('$''#'):
    print('Ошибка: название начинается на один из специальных символов.')
else:
    print('Файл назван верно')