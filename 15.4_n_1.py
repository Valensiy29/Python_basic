from abc import ABC, abstractmethod


class Auto(ABC):

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def signal(self):
        pass

class AutoMixin:

    def music(self):
        print('ту ту ту ту тууу ту туту туту туту ту')

class Boat(Auto):
    water = True
    earth = False

class Amfibi(Auto,AutoMixin):
    pass


car = Amfibi()
car.music()

# from abc import ABC, abstractmethod
#
#
# class MusicMixin:
#
#     def play_music(self):
#         print("""
#         I see trees of green
#         Red roses too
#         I see them bloom
#         For me and for you
#         And I think to myself
#         What a wonderful world
#         """)
#
#
# class Transport(ABC):
#
#     @abstractmethod
#     def ride_on_earth(self):
#         pass
#
#     @abstractmethod
#     def ride_on_water(self):
#         pass
#
#
# class Car(Transport):
#
#     def ride_on_earth(self):
#         print("Едем по земле")
#
#
# class Boat(Transport):
#
#     def ride_on_water(self):
#         print("Ходим по воде")
#
#
# class Amphibian(Car, Boat, MusicMixin):
#     pass
#
#
# amph_transport = Amphibian()
# amph_transport.ride_on_earth()
# amph_transport.ride_on_water()
# amph_transport.play_music()