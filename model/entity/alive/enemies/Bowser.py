import pygame
from pygame import Surface

from model.entity.alive.enemies.Monster import Monster


class Bowser(Monster):
    def __init__(self, x=0, y=0, width=0, height=0, images_existing=[], image_killed='', koef=0, side=False, lifes=0,
                 max_way=0, xvel=0, yvel=0, gravity=0, move_speed=0, left=False, right=False, up=False, on_ground=False,
                 changing=False):

        super().__init__(x, y, width, height, images_existing, image_killed,  lifes, koef, max_way, xvel, yvel, gravity,
                         move_speed, left, right, up, on_ground, changing)
        self.__side = side

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value

    def change_image(self):
        if self.time_changing:
            if self.time_changing % self.koef == 0:
                self.image = pygame.image.load(self.images_existing[int(not self.side)][self.time_changing // self.koef - 1])
            self.time_changing = -1
        else:
            self.time_changing = len(self.images_existing) * self.koef

    def killed(self, monsters, entities, blocks):
        if self.lifes == 0:
            if self.side:
                self.image = pygame.image.load(self.image_killed[0])
            else:
                self.image = pygame.image.load(self.image_killed[1])
            super().killed(monsters, entities, blocks)