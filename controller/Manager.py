import pygame
from pygame import Surface

from model.logic.LogicGame import LogicGame
from view.ViewBackgound import ViewBackground

win_width = 800
win_height = 640
background_color = (92, 146, 252)


def main():
    pygame.init()
    window = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption("Mario")
    background = Surface((win_width, win_height))
    ViewBackground.fill_view(background, background_color)
    timer = pygame.time.Clock()
    LogicGame.start_game_window(background, background_color, window, timer, during_game=False)

if __name__ == "__main__":
    main()
