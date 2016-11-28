import pygame

from model.entity.dead.Platform import Platform


class SimpleBlock(Platform):

    def __init__(self, x=0, y=0, width=0, height=0, image='', image_damage='', lifes=0):
        super().__init__(x, y, width, height)
        self.__image_damage=image_damage
        self.image = pygame.image.load(image)
        self.__lifes = lifes

    @property
    def lifes(self):
        return self.__lifes
    @lifes.setter
    def lifes(self, value):
        self.__lifes += value

    @property
    def image_damage(self):
        return self.__image_damage

    def decrease_block_lives(self, hero_power, block, blocks, entities):
        self.lifes = -hero_power
        if self.lifes == 1:
            self.image = pygame.image.load(self.__image_damage)
        if self.lifes <= 0:
            entities.remove(block)
            blocks.remove(self)
            del self
