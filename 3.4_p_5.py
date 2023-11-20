
violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
total = int(input('сколько песен'))


num = 0
sum = 0
for _ in range(total):
    songs = input('какие названия')
    for i in violator_songs:
        if i[0] == songs:
            sum += i[1]
        num += 1


print('общее звучание',round(sum,2))

