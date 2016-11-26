import pygame,sys
from pygame import *

from view.ViewBackgound import View


class LogicMenu:

    font=''
    height_game=0
    height_menu=0
    background_color=0
    color_active_text=0
    color_simple_text=0

    @staticmethod
    def show_lives(background, heroes):
        array=heroes.get_lives()
        font_menu = pygame.font.Font(LogicMenu.font, LogicMenu.height_game)
        for i in range(len(array)):
            View.blit_font(background,font_menu,array[i], 1, (0,0,0), background.get_width()//2+200*(i-1), 10)

    @staticmethod
    def get_points_menu():
        return [(270, 200, u'1 Player', 1),
                (270, 300, u'2 Players', 2),
                (270, 400, u'Settings', 3),
                (270, 500, u'Exit', 4),
                (200, 100, u'Welcome To Mario!', 0)]

    @staticmethod
    def menu(background, window, during_game=False):
        font_menu = pygame.font.Font(LogicMenu.font, LogicMenu.height_menu)
        point = 1
        if during_game:
            points = LogicMenu.get_points_during_menu()
        else:
            points = LogicMenu.get_points_menu()

        View.fill_view(background, LogicMenu.background_color)
        while True:
            LogicMenu.render(points, background, font_menu, point)
            for e in pygame.event.get():
                if e.type == QUIT:
                    sys.exit()
                if e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        return
                    if e.key == K_UP:
                        if point > 0:
                            point -= 1
                    if e.key == K_DOWN:
                        if point < len(points):
                            point += 1
                    if e.key == 13:
                        if point in [1, 2, 3, 4]:
                            return point
            View.blit_view(window, background, 0, 0)
            pygame.display.flip()

    @staticmethod
    def get_settings_points_menu(settings):
        return [[70, 380, u'Back', 1],
                [250, 100, u'%s' % chr(settings[0]), 2],
                [250, 170, u'%s' % chr(settings[1]), 3],
                [250, 240, u'%s' % chr(settings[2]), 4],
                [250, 310, u'%s' % chr(settings[3]), 5],
                [550, 100, u'%s' % chr(settings[4]), 6],
                [550, 170, u'%s' % chr(settings[5]), 7],
                [550, 240, u'%s' % chr(settings[6]), 8],
                [550, 310, u'%s' % chr(settings[7]), 9],
                [70, 100, u'Up', 0],
                [70, 170, u'Left', 0],
                [70, 240, u'Right', 0],
                [70, 310, u'Fire', 0],
                [250, 30, u'1 Player', 0],
                [550, 30, u'2 Player', 0],
                [70, 100, u'Up', 0],
                [70, 170, u'Left', 0],
                [70, 240, u'Right', 0]]

    @staticmethod
    def settings(background, window, settings, during_game):
        font_menu = pygame.font.Font(LogicMenu.font, LogicMenu.height_menu)
        point = 1
        points = LogicMenu.get_settings_points_menu(settings)
        View.fill_view(background, LogicMenu.background_color)
        while True:
            LogicMenu.render(points, background, font_menu, point)
            for e in pygame.event.get():
                if e.type == QUIT:
                    sys.exit()
                if e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        if during_game:
                            LogicMenu.menu(background, window, during_game=True)
                            return
                        LogicMenu.menu(background, window, during_game=False)
                        return

                    if e.key == K_UP:
                        if point > 0:
                            point -= 1
                    if e.key == K_DOWN:
                        if point < len(points)-1:
                            point += 1
                    if e.key == 13:
                        if point in [2, 3, 4, 5, 6, 7, 8, 9]:
                            string = LogicMenu.replace_button(points, point-1, settings)
                            if string:
                                settings[point - 1] = ord(string)
                                points[point-1][2] = u'%s' % string
                            View.fill_view(background, LogicMenu.background_color)
                        if point == 1:
                            if during_game:
                                LogicMenu.menu(background, window, during_game=True)
                                return
                            LogicMenu.menu(background, window, during_game=False)
                            return
            View.blit_view(window, background, 0, 0)
            pygame.display.flip()

    @staticmethod
    def get_points_during_menu():
        return [(250, 200, u'Settings', 1),
                (250, 300, u'Back to Game', 2),
                (250, 400, u'Finish Game', 3),
                (250, 500, u'Exit', 4),
                (330, 100, u'Menu', 0)]

    @staticmethod
    def render(punkts, surface, font, num_point):
        for punkt in punkts:
            x, y, text, point = punkt
            if num_point == point and num_point != 0:
                View.blit_font(surface, font, text, 1, LogicMenu.color_active_text, x, y)
            else:
                View.blit_font(surface, font, text, 1, LogicMenu.color_simple_text, x, y)

    @staticmethod
    def replace_button(points, i, settings):
        string = ""
        while True:
            for e in pygame.event.get():
                if e.type == QUIT:
                    sys.exit()
                if e.type == KEYDOWN:
                    if e.key == K_BACKSPACE:
                        string = string.replace(string[len(string)-1], "")
                    elif e.key == K_ESCAPE:
                        return string if LogicMenu.check_on_free(string, settings) and string \
                                      else points[i][2]
                    else:
                        string += chr(e.key)

    @staticmethod
    def check_on_free(value, settings):
        if len(value) == 1:
            keys = {
                ' ': ord(' '),
                '!': ord('!'),
                '"': ord('"'),
                '#': ord('#'),
                '$': ord('$'),
                '&': ord('&'),
                '(': ord('('),
                ')': ord(')'),
                '*': ord('*'),
                '+': ord('+'),
                ',': ord(','),
                '-': ord('-'),
                '.': ord('.'),
                '/': ord('/'),
                '0': ord('0'),
                '1': ord('1'),
                '2': ord('3'),
                '3': ord('3'),
                '4': ord('4'),
                '5': ord('5'),
                '6': ord('6'),
                '7': ord('7'),
                '8': ord('8'),
                '9': ord('9'),
                ':': ord(':'),
                ';': ord(';'),
                '<': ord('<'),
                '>': ord('>'),
                '=': ord('='),
                '?': ord('?'),
                '@': ord('@'),
                '[': ord('['),
                ']': ord(']'),
                '^': ord('^'),
                '_': ord('_'),
                "'": ord("'"),
                'a': ord('a'),
                'b': ord('b'),
                'c': ord('c'),
                'd': ord('d'),
                'e': ord('e'),
                'f': ord('f'),
                'g': ord('g'),
                'h': ord('h'),
                'i': ord('i'),
                'j': ord('j'),
                'k': ord('k'),
                'l': ord('l'),
                'm': ord('m'),
                'n': ord('n'),
                'o': ord('o'),
                'p': ord('p'),
                'q': ord('q'),
                'r': ord('r'),
                's': ord('s'),
                't': ord('t'),
                'u': ord('u'),
                'v': ord('v'),
                'w': ord('w'),
                'x': ord('x'),
                'y': ord('y'),
                'z': ord('z')
            }
            if keys.get(value):
                for e in settings:
                    if e == ord(value):
                        return False
                return True
            else:
                return False
        return False
