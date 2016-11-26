import pygame
from model.entity.dead.Platform import Platform


class BonusBlock(Platform):

    def __init__(self, x=0, y=0, width=0, height=0, images=[],image_simple='', koef=0,  activity=False, change_ability=False, type_bonus=0):
        super().__init__(x, y, width, height)
        self.__images = images
        self.__image_simple = image_simple
        self.image = pygame.image.load(images[0])
        self.__koef = koef
        self.__change_ability = change_ability
        self.__activity = activity

        self.__type_bonus = type_bonus

    @property
    def activity(self):
        return self.__activity

    @activity.setter
    def activity(self, value=False):
        self.__activity = value

    @property
    def change_ability(self):
        return self.__change_ability

    @change_ability.setter
    def change_ability(self, value=False):
        self.__change_ability = value

    @property
    def type_bonus(self):
        return self.__type_bonus

    @property
    def image_simple(self):
        return self.__image_simple

    @property
    def koef(self):
        return self.__koef

    @koef.setter
    def koef(self, value=0):
        self.__koef += value

    def set_koef(self, value=20):
        self.__koef += value

    def make_simple(self):
        self.image = pygame.image.load(self.image_simple)
        self.activity = self.change_ability = False

    def change_image(self):
        if self.koef==0:
            self.set_koef()
            self.__images.reverse()
            self.image = pygame.image.load(self.__images[0])
        else:
            self.koef = -1
