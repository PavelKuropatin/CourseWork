import  pygame
from pygame import *


class Live(sprite.Sprite):
    def __init__(self,  x=0, y=0, width=0, height=0, name_image=''):

        sprite.Sprite.__init__(self)
        # size and position
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.image = Surface((width, height))
        self.rect = Rect(x, y, width, height)

        self.image = pygame.image.load(name_image)
