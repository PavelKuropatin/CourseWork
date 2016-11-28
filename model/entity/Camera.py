from pygame import Rect


class Camera:

    def __init__(self, width=0, height=0, window_width=0, window_height=0):
        self.__window_width = window_width
        self.__window_height = window_height
        self.__window = Rect(0, 0, width, height)

    @property
    def window(self):
        return self.__window
    @window.setter
    def window(self,value_rect):
        self.__window = value_rect

    @property
    def window_width(self):
        return self.__window_width
    @window_width.setter
    def window_width(self, value):
        self.__window_width = value

    @property
    def window_height(self):
        return self.__window_height
    @window_height.setter
    def window_height(self, value):
        self.__window_height = value

    def shift_object(self, object_rect):
        return object_rect.move(self.window.topleft)

    def in_center(self, object_rect):
        left, top, _, _ = object_rect
        _, _, width_rect, height_rect = self.window
        left, top = -left + self.window_width // 2, -top + self.window_height // 2
        left = min(0, left) - 32
        left = max(-(self.window.width - self.window_width), left)
        top = max(-(self.window.height - self.window_height), top)
        top = min(0, top)
        self.window = Rect(left, top, width_rect, height_rect)
