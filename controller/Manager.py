import pygame
from pygame import Surface
from model.logic.LogicGame import LogicGame
from view.ViewBackgound import ViewBackground


def main():
    window_width = 800
    window_height = 640
    background_color = (92, 146, 252)
    pygame.init()
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Mario")
    background = Surface((window_width, window_height))
    ViewBackground.fill_view(background, background_color)
    timer = pygame.time.Clock()
    LogicGame.start_game_window(background, background_color, window, timer, during_game=False)

if __name__ == "__main__":
    main()
