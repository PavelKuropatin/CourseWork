from pygame import Surface, Rect, sprite


class Platform(sprite.Sprite):

    def __init__(self, x, y, width, height):
        sprite.Sprite.__init__(self)
        self.image = Surface((width, height))
        self.rect = Rect(x, y, width, height)
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
