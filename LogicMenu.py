import pygame,sys
from pygame import *

from model.entity.alive.heroes import Heroes
from view.ViewBackgound import View


class LogicMenu:

    @staticmethod
    def render(points, surface, font, num_point):
        for i in points:
            if num_point == i[3] and num_point != 0:
                surface.blit(font.render(i[2], 1, (250, 30, 250)), (i[0], i[1]))
            else:
                surface.blit(font.render(i[2], 1, (250, 250, 30)), (i[0], i[1]))

    @staticmethod
    def menu(background, window, settings):
        points = [(270, 200, u'1 Player', 1),
                            (270, 300, u'2 Players', 2),
                            (270, 400, u'Settings', 3),
                            (270, 500, u'Exit', 4),
                            (200, 100, u'Welcome To Mario!', 0)]
        font_menu = pygame.font.Font('data/coders_crux.ttf', 70)
        point = 1
        View.fill_view(background, (0, 100, 200))
        while True:
            LogicMenu.render(points, background, font_menu, point)
            for e in pygame.event.get():
                if e.type == QUIT:
                    sys.exit()
                if e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        sys.exit()
                    if e.key == K_UP:
                        if point > 0:
                            point -= 1
                    if e.key == K_DOWN:
                        if point < len(points):
                            point += 1
                    if e.key == 13:
                        if point == 1 or point == 2:
                            return point
                        if point == 3:
                            LogicMenu.settings(background, window, settings)
                            View.fill_view(background, (0, 100, 200))
                        if point == 4:
                            sys.exit()
            View.blit_view(window, background, 0, 0)
            pygame.display.flip()

    @staticmethod
    def settings(background, window, settings):
        font_menu = pygame.font.Font('data/coders_crux.ttf', 60)
        point = 1
        points = [[250, 100, u'%s' % chr(settings[0]), 1],
                [250, 170, u'%s' % chr(settings[1]), 2],
                [250, 240, u'%s' % chr(settings[2]), 3],
                [250, 310, u'%s' % chr(settings[3]), 4],
                [550, 100, u'%s' % chr(settings[4]), 5],
                [550, 170, u'%s' % chr(settings[5]), 6],
                [550, 240, u'%s' % chr(settings[6]), 7],
                [550, 310, u'%s' % chr(settings[7]), 8],
                [70, 380, u'Back', 9],
                [70, 100, u'Up', 0],
                [70, 170, u'Left', 0],
                [70, 240, u'Right', 0],
                [70, 310, u'Fire', 0],
                [250, 30, u'1 Player', 0],
                [550, 30, u'2 Player', 0],
                [70, 100, u'Up', 0],
                [70, 170, u'Left', 0],
                [70, 240, u'Right', 0]]
        View.fill_view(background, (0, 100, 200))
        while True:
            LogicMenu.render(points, background, font_menu, point)
            for e in pygame.event.get():
                if e.type == QUIT:
                    sys.exit()
                if e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        LogicMenu.menu(background, window, settings)
                        return
                    if e.key == K_UP:
                        if point > 0:
                            point -= 1
                    if e.key == K_DOWN:
                        if point < len(points)-1:
                            point += 1
                    if e.key == 13:
                        if point in [1, 2, 3, 4, 5, 6, 7, 8]:
                            string = LogicMenu.replace_button(points, point-1, settings)
                            if string:
                                settings[point - 1] = ord(string)
                                points[point-1][2] = u'%s' % string
                            View.fill_view(background, (0, 100, 200))
                        if point == 9:
                            LogicMenu.menu(background, window, settings)
                            return
            View.blit_view(window, background, 0, 0)
            pygame.display.flip()

    @staticmethod
    def during_game_menu(background, window, heroes):
        if isinstance(heroes, Heroes):
            font_menu = pygame.font.Font('data/coders_crux.ttf', 70)
            point = 1
            points = [(250, 200, u'Settings', 1),
                                (250, 300, u'Back to Game', 2),
                                (250, 400, u'Finish Game', 3),
                                (250, 500, u'Exit', 4),
                                (330, 100, u'Menu', 0)]
            View.fill_view(background, (0, 100, 200))
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
                            if point == 1:
                                LogicMenu.settings_during_game(background, window, heroes)
                                View.fill_view(background, (0, 100, 200))
                            if point == 2:
                                return
                            if point == 3:
                                return point
                            if point == 4:
                                sys.exit()

                View.blit_view(window, background, 0, 0)
                pygame.display.flip()

    @staticmethod
    def settings_during_game( background, window, heroes):
        if isinstance(heroes, Heroes):
            font_menu = pygame.font.Font('data/coders_crux.ttf', 60)
            point = 0
            View.fill_view(background, (0, 100, 200))
            points = [[70, 380, u'Back', 1],
                                [250, 100, u'%s' % chr(heroes.lst[0].key_up), 2],
                                [250, 170, u'%s' % chr(heroes.lst[0].key_left), 3],
                                [250, 240, u'%s' % chr(heroes.lst[0].key_right), 4],
                                [250, 310, u'%s' % chr(heroes.lst[0].key_fire), 5]]
            if len(heroes.lst) == 2:
                LogicMenu.add(points, [550, 100, u'%s' % chr(heroes.lst[1].key_up), 6],
                              [550, 170, u'%s' % chr(heroes.lst[1].key_left), 7],
                              [550, 240, u'%s' % chr(heroes.lst[1].key_right), 8],
                              [550, 310, u'%s' % chr(heroes.lst[1].key_fire), 9],
                              [70, 100, u'Up', 0],
                              [70, 170, u'Left', 0],
                              [70, 240, u'Right', 0],
                              [70, 310, u'Fire', 0],
                              [250, 30, u'1 Player', 0],
                              [550, 30, u'2 Player', 0])
            else:
                LogicMenu.add(points, [70, 100, u'Up', 0],
                              [70, 170, u'Left', 0],
                              [70, 240, u'Right', 0],
                              [70, 310, u'Fire', 0],
                              [250, 30, u'1 Player', 0])
                if heroes.lst[0].type == "hero2":
                        points[7][2] = u'2 Player'
            View.fill_view(background, (0, 100, 200))
            while True:
                LogicMenu.render(points, background, font_menu, point)
                for e in pygame.event.get():
                    if e.type == QUIT:
                        sys.exit()
                    if e.type == KEYDOWN:
                        if e.key == K_ESCAPE:
                            LogicMenu.during_game_menu(background, window, heroes)
                            return
                        if e.key == K_UP:
                            if point > 0:
                                point -= 1
                        if e.key == K_DOWN:
                            if point < len(points) - 1:
                                point += 1
                        if e.key == 13:
                            if point == 1:
                                LogicMenu.during_game_menu(background, window, heroes)
                                return
                            if point in [2, 3, 4, 5, 6, 7, 8, 9]:
                                string = LogicMenu.replace_button(points, point - 1, heroes.lst)
                                if string:
                                    if point == 2:
                                        heroes.lst[0].key_up = ord(string)
                                    if point == 3:
                                        heroes.lst[0].key_left = ord(string)
                                    if point == 4:
                                        heroes.lst[0].key_right = ord(string)
                                    if point == 5:
                                        heroes.lst[0].key_fire = ord(string)
                                    if point == 3:
                                        heroes.lst[1].key_up = ord(string)
                                    if point == 7:
                                        heroes.lst[1].key_left = ord(string)
                                    if point == 8:
                                        heroes.lst[1].key_right = ord(string)
                                    if point == 9:
                                        heroes.lst[1].key_fire = ord(string)
                                    points[point - 1][2] = u'%s' % string
                                    View.fill_view(background, (0, 100, 200))
                View.blit_view(window, background, 0, 0)
                pygame.display.flip()

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
                if not isinstance(settings[0], int):
                    for e in settings:
                        if e.key_up == ord(value) or e.key_left == ord(value) or e.key_right == ord(value):
                            return False
                    return True
                else:
                    for e in settings:
                        if e == ord(value):
                            return False
                    return True
            else:
                return False
        return False

    @staticmethod
    def get_key_press():
        for e in pygame.event.get():
            if e.type == KEYDOWN:
                return e.key
            else:
                return False

    @staticmethod
    def add(points, *args):
        for item in args:
            points.append(item)

    @staticmethod
    def show_lifes(lst, background):
        string = []
        for e in lst:
            string.append(u'%s - %d\n'%(e.type, e.lifes))
        print(string)
        font_menu = pygame.font.Font('data/coders_crux.ttf', 70)
        for e in string:
                background.blit(font_menu.render(e, 1, (250, 30, 250)), (100,200))