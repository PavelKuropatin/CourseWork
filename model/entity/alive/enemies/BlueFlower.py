import pygame
from pygame import Surface

from model.entity.alive.enemies.Monster import Monster


class BlueFlower(Monster):
    def __init__(self, x=0, y=0, width=0, height=0, images_existing=[], image_killed='', koef=0, koef_exist=0,
                 lifes=0, max_way=0, xvel=0, yvel=0, gravity=0, move_speed=0, left=False, right=False,
                 up=False, on_ground=True, changing=False):

        super().__init__(x, y, width, height, images_existing*koef_exist, image_killed,  lifes, koef, max_way, xvel, yvel, gravity,
                         move_speed, left, right, up, on_ground, changing)
        self.__amount_images_existing = len(images_existing*koef_exist) * koef
        self.__images_indexes = [i for i in range(0, height, 2)]
        self.check=True

    @property
    def amount_images_existing(self):
        return self.__amount_images_existing

    @amount_images_existing.setter
    def amount_images_existing(self, value=0):
        self.__amount_images_existing = value

    def change_image(self):
        if self.check:
            self.rect.y += 1
        else:
            self.rect.y -=1
        self.image = pygame.image.load(self.images_existing[self.amount_images_existing // self.koef - 1])
        self.amount_images_existing -= 1
        if self.amount_images_existing == 0:
            self.check = not (self.check)
            self.amount_images_existing = len(self.images_existing) * self.koef

    def killed(self, monsters, entities, blocks):
        if self.lifes == 0:
            self.image = pygame.image.load(self.image_killed)
            super().killed(monsters, entities, blocks)