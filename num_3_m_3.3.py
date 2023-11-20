decode = []
l_pack = 0
pack = int(input('сколько пакетов'))
for _ in range(pack):
    d_decode = []
    er_pack = 0
    for num in range(4):
        bit = int(input('бит'))
        d_decode.append(bit)
        if bit < 0:
            er_pack += 1
    if er_pack <= 1:
        decode.extend(d_decode)
    else:
        l_pack += 1
print(decode)
print(decode.count(-1))
print(l_pack)