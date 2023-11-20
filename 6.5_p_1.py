violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

time = 0
count = int(input('введите кол-во песен'))

for i in range(count):
    songs = input('введите название песни')
    time += violator_songs[songs]
    print(violator_songs[songs])
print('общее время звучания', time)