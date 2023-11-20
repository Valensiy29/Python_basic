import math
# def place(rad,sid,side):
#     return tuple(side + 2 * (math.pi * rad ** 2)), tuple(side)
#
# rad = int(input('введите радиус'))
# sid = int(input('введите высоtu'))
# side = math.pi * 2 * rad * sid
# place(rad,sid,side)
#
# print(place)

radius_in = int(input("Введите радиус: "))
height_in = int(input("Введите высоту: "))


def cylinder_math(r, height):
    side = 2 * math.pi * r * height
    full = side + 2 * math.pi * r ** 2
    return side, full


bot_area, full_area = cylinder_math(radius_in, height_in)
print(bot_area, full_area)