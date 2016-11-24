from pygame import Color


class View:

    @staticmethod
    def fill_view(background, color):
        background.fill(color)

    @staticmethod
    def blit_view(window,background, x, y):
        window.blit(background, (x, y))