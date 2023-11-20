film = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
loved_film = []
love = []
question = int(input('сколько фильмов хотите добавить'))
twerd = 0

for num in range(question):
    choose = input('введите название фильма')
    loved_film.append(choose)
for i,number in enumerate(film):
    if loved_film[twerd] == film[i]:
        love.append(number)
        twerd += 1

print(love)