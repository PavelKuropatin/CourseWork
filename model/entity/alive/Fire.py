import pygame
from pygame import *
from model.entity.alive.Character import Character


class Fire(Character):

        def __init__(self, x=0, y=0, width=0, height=0, image='', side=False, power=0, xvel=0, yvel=0, gravity=0,
                     move_speed=0, left=False, right=False, up=False, on_ground=False, max_way=0, alive=False):

            super().__init__(x, y, width, height, left, right, up, on_ground, xvel, yvel, move_speed, gravity)
            self.image = pygame.image.load(image)
            self.__power = power
            self.__alive = alive
            self.__max_way = max_way
            self.__side = side

        @property
        def max_way(self):
            return self.__max_way

        @property
        def power(self):
            return self.__power

        @property
        def side(self):
            return self.__side
        @side.setter
        def side(self, value):
            self.__side = value

        @property
        def alive(self):
            return self.__alive
        @alive.setter
        def alive(self, value=False):
            self.__alive = value

        def killed(self, monsters, entities):
            entities.remove(self)
            monsters.remove(self)
            del self
