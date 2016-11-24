from pygame import sprite, Rect, Surface
from model.entity.alive.Character import Character
import pygame


class Hero(Character):

    def __init__(self,  x=0, y=0, width=0, height=0, keys=[], type='', name_image='',
                        side=False, power=1, lifes=3, super_hero=False,
                        time_flower_activity=0,
                        left=False, right=False, up=False, on_ground=False, xvel=0, yvel=0,
                        move_speed=4, jump_power=16, gravity=1):
        super().__init__(x, y, width, height, left, right, up, on_ground, xvel, yvel, move_speed, gravity, lifes)
        self.__type = type
        self.__side = side
        self.__power = power
        self.__super_hero = super_hero
        self.__time_flower_activity = time_flower_activity

        self.__jump_power = jump_power

        self.__key_up = keys[0]
        self.__key_left = keys[1]
        self.__key_right = keys[2]
        self.__key_fire = keys[3]
        self.image = pygame.image.load(name_image)

    @property
    def type(self):
        return self.__type

    @property
    def power(self):
        return self.__power

    @property
    def jump_power(self):
        return self.__jump_power

    @jump_power.setter
    def jump_power(self, value):
        self.__jump_power = value


    @power.setter
    def power(self, value):
        self.__power = value

    @property
    def super_hero(self):
        return self.__super_hero

    @super_hero.setter
    def super_hero(self, value=False):
        self.__super_hero = value

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value

    @property
    def time_flower_activity(self):
        return self.__time_flower_activity

    @time_flower_activity.setter
    def time_flower_activity(self, value=0):
        self.__time_flower_activity = value



    @property
    def key_fire(self):
            return self.__key_fire

    @key_fire.setter
    def key_fire(self, value):
        self.__key_fire = value

    @property
    def key_up(self):
        return self.__key_up

    @property
    def key_left(self):
        return self.__key_left

    @property
    def key_right(self):
        return self.__key_right

    @property
    def key_up(self):
        return self.__key_up

    @key_up.setter
    def key_up(self, value):
        self.__key_up = value

    @property
    def key_left(self):
        return self.__key_left

    @key_left.setter
    def key_left(self, value):
        self.__key_left = value

    @property
    def key_right(self):
        return self.__key_right

    @key_right.setter
    def key_right(self, value):
        self.__key_right = value

    def move_to_start(self):
        self.rect.x = self.x
        self.rect.y = self.y


    def get_super_jump(self, value, bonus_time):
        # self.rect.x = 801
        # self.rect.y = 200
        # self.rect.height = int(value * self.__HEIGHT)
        # self.rect.width = int(value * self.__WIDTH)
        # self.image = pygame.image.load('mario/hero1_up.png')
        self.__jump_power = int(self.__jump_power * value)
        self.time_flower_activity = bonus_time

    def get_simple_jump(self, value, bonus_time):
        self.jump_power = 16

    def become_simple_mario(self):
        # self.rect.x = 801
        # self.rect.y = 200
        # self.rect.height = int(value * self.__HEIGHT)
        # self.rect.width = int(value * self.__WIDTH)
        # self.image = pygame.image.load('mario/hero1_up.png')
        self.__jump_power = 16
        self.__power = 1
        self.__super_hero = False
        self.__time_flower_activity = 0
