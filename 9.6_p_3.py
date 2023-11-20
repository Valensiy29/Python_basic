from operator import attrgetter

def rarity_zen(zen):
    new_rar = []
    stop_sim = ['!',' ','\n','*',"'",',','-','.']
    zen_remove = []
    rarity_z = []
    rarity = {}
    counter_word = 0
    counter_num = 0
    counter_lines = 0
    for i in zen:
        zen_remove.append(i)
        counter_lines += 1
        for word in i.lower():
            rarity_z.append(word)
            if str(word) and word not in stop_sim:
                counter_word += 1
                rarity[word] = rarity_z.count(word)
                new_rar.append(rarity.values)
                victory = min(rarity.items())
            # elif int(word):
            #      counter_num += 1


    return counter_lines, counter_word, counter_num, victory



zen = open('zen.txt', 'r')
rarity_zen(zen)