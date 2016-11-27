from pygame import time
from model.entity.alive.Character import Character


class Monster(Character):

    def __init__(self, x=0, y=0, width=0, height=0,images_existing=[], image_killed='', lifes=0, koef=0, max_way=0,
                 xvel=0, yvel=0, gravity=0, move_speed=0,left=False, right=False, up=False, on_ground=False,
                 changing=False):

        super().__init__(x, y, width, height, left, right, up, on_ground, xvel, yvel, move_speed, gravity, lifes)
        self.__max_way = max_way
        self.__changing = changing
        self.__koef = koef
        self.__image_killed = image_killed
        self.__images_existing = images_existing
        self.__time_changing = len(self.__images_existing) * koef

    @property
    def time_changing(self):
        return self.__time_changing

    @time_changing.setter
    def time_changing(self, value):
        self.__time_changing += value

    @property
    def changing(self):
        return self.__changing

    @property
    def koef(self):
        return self.__koef

    @property
    def max_way(self):
        return self.__max_way

    @property
    def images_existing(self):
        return self.__images_existing

    @property
    def image_killed(self):
        return self.__image_killed

    @changing.setter
    def changing(self, value=False):
        self.__changing = value\

    @max_way.setter
    def max_way(self, value=False):
        self.__max_way = value

    def killed(self,monsters, entities, blocks):
        self.rect.y += self.rect.height // 2
        self.xvel = 0
        self.changing = False

        monsters.remove(self)
        blocks.remove(self)
        time.wait(1000)
        entities.remove(self)
        del self






