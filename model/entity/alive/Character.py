from pygame import *


class Character(sprite.Sprite):

    def __init__(self,  x=0, y=0, width=0, height=0, left=False, right=False, up=False, on_ground=False, xvel=0, yvel=0,
                 move_speed=0, gravity=0, lifes=0):

        sprite.Sprite.__init__(self)
        self.__lifes = lifes
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.image = Surface((width, height))
        self.rect = Rect(x, y, width, height)
        self.__left = left
        self.__right = right
        self.__up = up
        self.__on_ground = on_ground
        self.xvel = xvel
        self.yvel = yvel
        self.__move_speed = move_speed
        self.__gravity = gravity

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def lifes(self):
        return self.__lifes
    @lifes.setter
    def lifes(self, value):
        self.__lifes += value

    @property
    def left(self):
        return self.__left
    @left.setter
    def left(self, value):
        self.__left = value

    @property
    def right(self):
        return self.__right
    @right.setter
    def right(self, value):
        self.__right = value

    @property
    def up(self):
        return self.__up
    @up.setter
    def up(self, value):
        self.__up = value

    @property
    def gravity(self):
        return self.__gravity
    @gravity.setter
    def gravity(self, value):
        self.__gravity = value

    @property
    def on_ground(self):
        return self.__on_ground
    @on_ground.setter
    def on_ground(self, value):
        self.__on_ground = value

    @property
    def move_speed(self):
        return self.__move_speed

    @move_speed.setter
    def move_speed(self, value):
        self.__move_speed = value