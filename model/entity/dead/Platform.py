from pygame import Surface, Rect, sprite


class Platform(sprite.Sprite):

    def __init__(self, x=0, y=0, width=0, height=0):
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

    def killed(self, entities, blocks):
        entities.remove(self)
        blocks.remove(self)
        del self
