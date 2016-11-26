import pygame

class View:

    @staticmethod
    def fill_view(background, color):
        background.fill(color)

    @staticmethod
    def blit_view(window,background, x, y):
        window.blit(background, (x, y))

    @staticmethod
    def blit_font(background,font,text,value,color,x,y):
        background.blit(font.render(text, value, color), (x, y))
        pass