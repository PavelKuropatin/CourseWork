import pygame
from pygame import *
from model.entity.alive.enemies.Monster import Monster


class Slub(Monster):

    def __init__(self, x=0, y=0, width=0, height=0, images_existing=[], image_killed='', koef=0, lifes=0, max_way=0,
                 xvel=0, yvel=0, gravity=0, move_speed=0, left=False, right=False, up=False, on_ground=False,
                 changing=False):

        super().__init__(x, y, width, height, images_existing, image_killed, lifes, koef, max_way, xvel, yvel, gravity,
                         move_speed, left, right, up, on_ground, changing)

    def change_image(self):
        if self.time_changing:
            if self.time_changing % self.koef == 0:
                self.image = pygame.image.load(self.images_existing[self.time_changing // self.koef - 1])
            self.time_changing = -1
        else:
            self.time_changing = len(self.images_existing) * self.koef

    def killed(self, monsters, entities, blocks):
        if self.lifes == 0:
            if not isinstance(self.image_killed, list):
                self.image = pygame.image.load(self.image_killed)
                pass
            else:
                if self.side:
                    self.image = pygame.image.load(self.image_killed[0])
                    pass
                else:
                    self.image = pygame.image.load(self.image_killed[1])
                    pass
            super().killed(monsters, entities, blocks)
