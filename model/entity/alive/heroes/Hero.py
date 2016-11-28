from pygame import sprite, Rect, Surface
from model.entity.alive.Character import Character
import pygame


class Hero(Character):

    def __init__(self,  x=0, y=0, width=0, height=0, keys=[], type='', name_image='', side=False, power=0, lifes=0,
                 super_hero=False, time_flower_activity=0, time_mushroom_activity=0, left=False, right=False, up=False,
                 on_ground=False, xvel=0, yvel=0, move_speed=0, jump_power=0, gravity=0, fire_ability=False,
                 flower_ability=False):

        super().__init__(x, y, width, height, left, right, up, on_ground, xvel, yvel, move_speed, gravity, lifes)
        self.__type = type
        self.__side = side
        self.__power = power
        self.__super_hero = super_hero
        self.__time_flower_activity = time_flower_activity
        self.__time_mushroom_activity = time_mushroom_activity
        self.__fire_ability = fire_ability
        self.__flower_ability = flower_ability
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
    def fire_ability(self):
        return self.__fire_ability
    @fire_ability.setter
    def fire_ability(self, value):
        self.__fire_ability = value

    @property
    def flower_ability(self):
        return self.__flower_ability
    @flower_ability.setter
    def flower_ability(self, value):
        self.__flower_ability = value

    @property
    def jump_power(self):
        return self.__jump_power
    @jump_power.setter
    def jump_power(self, value):
        self.__jump_power = value

    @property
    def power(self):
        return self.__power
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
        self.__time_flower_activity += value

    @property
    def time_mushroom_activity(self):
        return self.__time_mushroom_activity
    @time_mushroom_activity.setter
    def time_mushroom_activity(self, value=0):
        self.__time_mushroom_activity += value

    @property
    def key_fire(self):
            return self.__key_fire
    @key_fire.setter
    def key_fire(self, value):
        self.__key_fire = value

    @property
    def key_up(self):
        return self.__key_up
    @key_up.setter
    def key_up(self, value):
        self.__key_up = value

    @property
    def key_left(self):
        return self.__key_left
    @property
    def key_left(self):
        return self.__key_left

    @property
    def key_right(self):
        return self.__key_right
    @key_right.setter
    def key_right(self, value):
        self.__key_right = value

    def move_to_start(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def get_super_jump(self, value=0):
        self.jump_power = int(self.jump_power * value)
        self.flower_ability = True

    def get_simple_jump(self, value=16):
        self.jump_power = value
        self.flower_ability = False

    def set_fire_ability(self):
        self.fire_ability = False

    def update_bonus(self):
        if self.flower_ability:
            if self.time_flower_activity == 0:
                self.get_simple_jump()
            else:
                self.time_flower_activity = -1
        if self.fire_ability:
            if self.time_mushroom_activity == 0:
                self.set_fire_ability()
            else:
                self.time_mushroom_activity = -1
