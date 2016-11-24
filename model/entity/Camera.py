from pygame import Rect

class Camera:
    def __init__(self, width, height):
        self.__window = Rect(0, 0, width, height)

    @property
    def window(self):
        return self.__window

    @window.setter
    def window(self,value_rect):
        self.__window = value_rect

    def shift_object(self, target):
        return target.rect.move(self.window.topleft)


