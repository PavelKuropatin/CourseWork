import pygame
from pygame import Surface

from model.logic.LogicGame import LogicGame
from view.ViewBackgound import View
from model.entity.alive.heroes.Heroes import Heroes

win_width = 800
win_height = 640
background_color = (92, 146, 252)


def main():
    pygame.init()

    window = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption("Mario")
    background = Surface((win_width, win_height))
    View.fill_view(background, background_color)

    settings = [119, 97, 100, 102, 105, 106, 108, 59]

    timer = pygame.time.Clock()
    LogicGame.startGameWindow(settings, background, background_color, window, timer)


if __name__ == "__main__":
    main()
