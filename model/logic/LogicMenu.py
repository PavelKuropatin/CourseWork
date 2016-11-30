import pygame,sys
from pygame import *
from view.ViewBackgound import ViewBackground


class LogicMenu:

    font = ''
    height_game = 0
    height_menu = 0
    background_color = (0, 0, 0)
    color_active_text = (0, 0, 0)
    color_simple_text = (0, 0, 0)

    @staticmethod
    def show_interface(background, heroes_lives, level):
        font_menu = pygame.font.Font(LogicMenu.font, LogicMenu.height_game)
        ViewBackground.blit_font(background, font_menu, u'Level %d' % (level), 1, (0, 0, 0), 10, 10)
        for i in range(len(heroes_lives)):
            ViewBackground.blit_font(background, font_menu, heroes_lives[i], 1, (0, 0, 0),
                                         background.get_width()//2+200*(i-1), 10)

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
        ViewBackground.fill_view(background, LogicMenu.background_color)
        while True:
            LogicMenu.render(points, background, font_menu, point)
            for e in pygame.event.get():
                if e.type == QUIT:
                    sys.exit()
                if e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        return
                    if e.key == K_UP:
                        if point > 1:
                            point -= 1
                    if e.key == K_DOWN:
                        if point < 4:
                            point += 1
                    if e.key == 13:
                        if point in [1, 2, 3, 4]:
                            return point
            ViewBackground.blit_view(window, background, 0, 0)
            pygame.display.flip()

    @staticmethod
    def get_settings_points_menu(settings):
        values=[]
        keys = {
            'space': K_SPACE,
            'tab': K_TAB,
            'right ctrl': K_RCTRL,
            'left ctrl': K_LCTRL,
            'up': K_UP,
            'down': K_DOWN,
            'left': K_LEFT,
            'right': K_RIGHT,
            'delete': K_DELETE,
            'backspace': K_BACKSPACE,
            'f1': K_F1,
            'f2': K_F2,
            'f3': K_F3,
            'f4': K_F4,
            'f5': K_F5,
            'f6': K_F6,
            'f7': K_F7,
            'f8': K_F8,
            'f9': K_F9,
            'f10': K_F10,
            'f11': K_F11,
            'f12': K_F12,
            'f13': K_F13,
            'f14': K_F14,
            'caps lock': K_CAPSLOCK,
            'right shift': K_RSHIFT,
            'left shift': K_LSHIFT,
            'left alt': K_LALT,
            'right alt': K_RALT,
            'menu': K_MENU,
            'insert': K_INSERT,
            'print screen': K_PRINT,
            'end': K_END,
            'page up': K_PAGEUP,
            'page down': K_PAGEDOWN,
            'pause': K_PAUSE,
            '[0]': K_KP0,
            '[1]': K_KP1,
            '[2]': K_KP2,
            '[3]': K_KP3,
            '[4]': K_KP4,
            '[5]': K_KP5,
            '[6]': K_KP6,
            '[7]': K_KP7,
            '[8]': K_KP8,
            '[9]': K_KP9,
            'enter': K_KP_ENTER,
            '[/]': K_KP_DIVIDE,
            '[+]': K_KP_PLUS,
            '[-]': K_KP_MINUS,
            '[*]': K_KP_MULTIPLY,
            '[.]': K_KP_PERIOD,
            'numlock': K_NUMLOCK
        }
        items = keys.items()
        for s in settings:
            for k, v in items:
                if v == s:
                    values.append(k)
                    break
            else:
                    values.append(chr(s))
        return [[50, 380, u'Back', 1],
                [250, 100, u'%s' % values[0], 2],
                [250, 170, u'%s' % values[1], 3],
                [250, 240, u'%s' % values[2], 4],
                [250, 310, u'%s' % values[3], 5],
                [550, 100, u'%s' % values[4], 6],
                [550, 170, u'%s' % values[5], 7],
                [550, 240, u'%s' % values[6], 8],
                [550, 310, u'%s' % values[7], 9],
                [50, 100, u'Up', 0],
                [50, 170, u'Left', 0],
                [50, 240, u'Right', 0],
                [50, 310, u'Fire', 0],
                [250, 30, u'1 Player', 0],
                [550, 30, u'2 Player', 0],
                [50, 100, u'Up', 0],
                [50, 170, u'Left', 0],
                [50, 240, u'Right', 0],
                [50, 490, u'To change button press Enter', 0],
                [50, 540, u'To install selected button', 0],
                [50, 580, u'press Escape', 0]]

    @staticmethod
    def settings(background, window, settings, during_game):
        font_menu = pygame.font.Font(LogicMenu.font, LogicMenu.height_menu)
        point = 1
        points = LogicMenu.get_settings_points_menu(settings)
        ViewBackground.fill_view(background, LogicMenu.background_color)
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
                        if point > 1:
                            point -= 1
                    if e.key == K_DOWN:
                        if point < 9:
                            point += 1
                    if point in [2, 3, 4, 5] and e.key == K_RIGHT:
                        point += 4
                    if point in [6, 7, 8, 9] and e.key == K_LEFT:
                        point -= 4
                    if e.key == 13:
                        if point in [2, 3, 4, 5, 6, 7, 8, 9]:
                            LogicMenu.replace_button(background, window, points, point, settings)
                        if point == 1:
                            if during_game:
                                LogicMenu.menu(background, window, during_game=True)
                                return
                            LogicMenu.menu(background, window, during_game=False)
                            return
            ViewBackground.blit_view(window, background, 0, 0)
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
                ViewBackground.blit_font(surface, font, text, 1, LogicMenu.color_active_text, x, y)
            else:
                ViewBackground.blit_font(surface, font, text, 1, LogicMenu.color_simple_text, x, y)

    @staticmethod
    def replace_button(background, window, points, point, settings):
        font_menu = pygame.font.Font(LogicMenu.font, LogicMenu.height_menu)
        while True:
            LogicMenu.render(points, background, font_menu, point)
            for e in pygame.event.get():
                if e.type == QUIT:
                    sys.exit()
                if e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        return
                    else:
                        for s in settings:
                            if s == e.key:
                                break
                        else:
                            settings[point - 2] = e.key
                            points[point - 1][2] = u'%s' % pygame.key.name(e.key)
                        ViewBackground.fill_view(background, LogicMenu.background_color)
            ViewBackground.blit_view(window, background, 0, 0)
            pygame.display.flip()
