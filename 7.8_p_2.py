def is_prime(need_prime):
    prime = []
    for i_num,i_index in enumerate(need_prime):
        new = need_prime[i_num:]
        count = 0
        for i_n in new:
            if i_num / i_n == 0:
                prime.append(i_num)
                # count += 1
                # if count == 1:
                #
                return prime




print(is_prime(([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
