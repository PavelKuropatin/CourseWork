import pygame

from model.entity.dead.Platform import Platform


class Flower(Platform):
    def __init__(self, x=0, y=0, width=0, height=0, start_image='', images_appearing=[],images_existing=[],
                 time_activity=0, change_ability=True, activity=True):

        super().__init__(x, y + 32, width, height)
        self.image = pygame.image.load(start_image)

        self.__images_appearing = images_appearing
        self.__amount_images_appearing = len(self.__images_appearing)

        self.__images_existing = images_existing
        self.__amount_images_existing = len(self.__images_existing) * 30

        self.__change_ability = change_ability
        self.__activity = activity
        self.__time_activity = time_activity

    @property
    def time_activity(self):
        return self.__time_activity

    @property
    def images_appearing(self):
        return self.__images_appearing

    @property
    def images_existing(self):
        return self.__images_existing

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
    def amount_images_appearing(self):
        return self.__amount_images_appearing

    @amount_images_appearing.setter
    def amount_images_appearing(self, value=0):
        self.__amount_images_appearing += value

    @property
    def amount_images_existing(self):
        return self.__amount_images_existing

    @amount_images_existing.setter
    def amount_images_existing(self, value=0):
        self.__amount_images_existing += value

    def appear_flower(self):
        self.image = pygame.image.load(self.images_appearing[self.amount_images_appearing - 2])
        self.amount_images_appearing = -1

    def exist_flower(self):
        self.image = pygame.image.load(self.images_existing[self.amount_images_existing // 30 - 2])
        if self.amount_images_existing != 0:
            self.amount_images_existing = -1
        else:
            self.amount_images_existing = len(self.images_existing) * 30





