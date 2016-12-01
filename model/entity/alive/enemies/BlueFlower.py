import pygame
from model.entity.alive.enemies.Monster import Monster


class BlueFlower(Monster):
    def __init__(self, x=0, y=0, width=0, height=0, images_existing=[], image_killed='', koef=0, koef_exist=0,
                 lifes=0, max_way=0, xvel=0, yvel=0, gravity=0, move_speed=0, left=False, right=False,
                 up=False, on_ground=True, alive=False, moving=False):

        super().__init__(x, y, width, height, images_existing*koef_exist, image_killed,  lifes, koef, max_way, xvel, yvel, gravity,
                         move_speed, left, right, up, on_ground, alive)
        self.__moving=moving

    @property
    def moving(self):
        return self.__moving


    @moving.setter
    def moving(self, value):
        self.__moving = value

    def change_image(self):
        if self.moving:
            self.rect.y += 1
        else:
            self.rect.y -=1
        self.image = pygame.image.load(self.images_existing[self.time_changing // self.koef - 1])
        self.time_changing -= 1
        if self.time_changing == 0:
            self.moving = not (self.moving)
            self.time_changing = len(self.images_existing) * self.koef

    def killed(self, monsters, entities, blocks):
        if self.lifes == 0:
            self.image = pygame.image.load(self.image_killed)
            super().killed(monsters, entities, blocks)