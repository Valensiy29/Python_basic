def orlean(file,file_w):
    need_score = 0
    counter = 0
    for i in file:
        if len(i) == 2:
            need_score += int(i)
            print(need_score)
        winners = {}
        guests = i.split()
        if len(guests) == 3:
            winners[guests[0], guests[1]] = guests[2]
            print(winners)
            if int(guests[2]) > need_score:
                surname = 'sdafgaeragerg'
                counter += 1
                file_w.write(str(counter) + surname)



file_w = open('second_tour.txt','a')
file = open('first_tour.txt','r')
orlean(file,file_w)