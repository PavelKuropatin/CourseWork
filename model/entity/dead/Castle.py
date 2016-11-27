import pygame

from model.entity.dead.Platform import Platform


class Castle(Platform):

    def __init__(self, x=0, y=0, width=0, height=0, image='', finish_block=False):
        super().__init__(x, y, width, height)
        self.image = pygame.image.load(image)
        self.__width = width
        self.__finish_block = finish_block

    @property
    def width(self):
        return self.__width

    @property
    def finish_block(self):
        return self.__finish_block
