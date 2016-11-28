import pygame
from model.entity.dead.Platform import Platform


class Nature(Platform):

    def __init__(self, x=0, y=0, width=0, height=0, image=''):
        super().__init__(x, y, width, height)
        self.image = pygame.image.load(image)
