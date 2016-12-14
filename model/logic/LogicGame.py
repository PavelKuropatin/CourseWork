import pygame
from pygame import *
import threading
import sys
from utility.Camera import Camera
from utility.LevelGenerator import LevelGenerator
from model.entity.alive.heroes.Hero import Hero
from model.logic.LogicHero import LogicHero
from model.logic.LogicMenu import LogicMenu
from model.logic.LogicMonster import LogicMonster
from view.ViewBackgound import ViewBackground
from model.entity.alive.heroes.Heroes import Heroes
from model.entity.alive.enemies.Monster import Monster
import random

class LogicGame:

    @staticmethod
    def start_game_window(background, background_color, window, timer, during_game=False):
        settings = [K_w, K_a, K_d, K_f, K_UP, K_LEFT, K_RIGHT, K_RCTRL]
        LogicMenu.font = "data/coders_crux.ttf"
        LogicMenu.height_menu = 60
        LogicMenu.height_game = 40
        LogicMenu.background_color = background_color
        LogicMenu.color_active_text = (250, 30, 250)
        LogicMenu.color_simple_text = (250, 250, 30)
        while True:
            choice = LogicMenu.menu(background, window, during_game=False)
            if choice == 1 or choice == 2:

                ''' Creating Heroes'''
                heroes = Heroes()
                hero1 = Hero(x=170, y=500, width=22, height=31, keys=settings[:4], type="hero1", animation_koef=3,
                             animation_right=['data/r1.png', 'data/r2.png', 'data/r3.png',
                                              'data/r4.png', 'data/r5.png'],
                             animation_left=['data/l1.png', 'data/l2.png', 'data/l3.png',
                                             'data/l4.png', 'data/l5.png'],
                             animation_jump_left='data/jl.png', animation_jump_right='data/jr.png',
                             animation_jump='data/j.png', side=False, power=1, lifes=3,
                             time_flower_activity=0, time_mushroom_activity=0, left=False, right=False, up=False,
                             on_ground=False, xvel=0, yvel=0, move_speed=4, jump_power=16, gravity=1,
                             fire_ability=False, flower_ability=False)
                heroes.append(hero1)
                if choice == 2:
                    hero2 = Hero(x=270, y=500, width=22, height=31, keys=settings[4:], type="hero2", animation_koef=3,
                                 animation_right=['data/r1.png', 'data/r2.png', 'data/r3.png',
                                                  'data/r4.png', 'data/r5.png'],
                                 animation_left=['data/l1.png', 'data/l2.png', 'data/l3.png',
                                                 'data/l4.png', 'data/l5.png'],
                                 animation_jump_left='data/jl.png', animation_jump_right='data/jr.png',
                                 animation_jump='data/j.png', side=False, power=1, lifes=3,
                                 time_flower_activity=0, time_mushroom_activity=0, left=False, right=False, up=False,
                                 on_ground=False, xvel=0, yvel=0, move_speed=4, jump_power=16, gravity=1,
                                 fire_ability=False, flower_ability=False)
                    heroes.append(hero2)
                generator = LevelGenerator(platform_width=32, platform_height=32,
                                           levels=['data/level1.txt', 'data/level2.txt','data/level3.txt'],
                                           level='', number_level=2)

                '''Start GAME'''
                LogicGame.start_game(settings, generator, background, window, timer, heroes, during_game=True)

            if choice == 3:

                ''' Move to settings'''
                if not during_game:
                    LogicMenu.settings(background, window, settings, during_game)
                    ViewBackground.fill_view(background, background_color)

            if choice == 4:

                ''' Exit Game'''
                sys.exit()

    @staticmethod
    def start_game(settings, generator, background, window, timer, heroes, during_game=True):

        if generator.number_level == generator.max_level:
            LogicGame.finish_game(background, window, 'data/lmfao.mp3')
            LogicGame.clear_data(heroes)
        else:
            entities = pygame.sprite.Group()
            for h in heroes.lst:
                entities.add(h)
            nature = pygame.sprite.Group()
            monsters = pygame.sprite.Group()
            platforms = []
            result_level = [False]

            '''Window Set'''
            generator.generate_level(entities, platforms, monsters, nature)
            level_width = len(generator.level[len(generator.level)-1]) * generator.platform_width
            level_height = len(generator.level) * generator.platform_height
            camera = Camera(level_width, level_height, background.get_width(), background.get_height())

            while True:

                button = LogicHero.check_press_key(heroes, entities, monsters)

                '''Show Menu During Game'''
                if button:
                    choice = LogicMenu.menu(background, window, during_game=True)

                    if choice == 1:
                        ''' Move To Settings During Game'''
                        LogicMenu.settings(background, window, settings, during_game=True)
                        heroes.update_keys(settings)
                        ViewBackground.fill_view(background, LogicMenu.background_color)

                    if choice == 3:
                        ''' Finish Existing Game'''
                        if during_game:
                            del generator
                            LogicGame.clear_data(heroes, entities, monsters, nature)
                            break

                    if choice == 4:
                        ''' Exit Game'''
                        sys.exit()

                '''Creating Threads'''
                t1 = threading.Thread(target=LogicHero.update_heroes, args=(heroes, platforms, entities, monsters,
                                                                            result_level))
                t1.start()
                t2 = threading.Thread(target=LogicMonster.update_monster, args=(monsters, platforms, entities, heroes))
                t2.start()
                timer.tick(1000)
                '''Set Background'''
                ViewBackground.blit_view(window, background, 0, 0)

                if result_level[0]:
                    heroes.set_default_settings()
                    LogicGame.clear_data(heroes, entities=entities, monsters=monsters, nature=nature, during_game=True)
                    LogicGame.start_game(settings, generator, background, window, timer, heroes, during_game=True)
                    result_level[0] = False
                    break

                '''Check On Existing Heroes'''
                if heroes.not_exist():
                    return

                '''Centering Camera'''
                camera.in_center(heroes.set_last_hero().rect)

                '''Draw objects'''
                for n in nature:
                    value = camera.shift_object(n.rect)
                    ViewBackground.blit_view(window, n.image, value.x, value.y)
                for m in monsters:
                    if isinstance(m, Monster):
                        value = camera.shift_object(m.rect)
                        ViewBackground.blit_view(window, m.image, value.x, value.y)
                for e in entities:
                    if not isinstance(e, Monster):
                        value = camera.shift_object(e.rect)
                        ViewBackground.blit_view(window, e.image, value.x, value.y)


                '''Update Background'''
                ViewBackground.fill_view(background, LogicMenu.background_color)

                '''Show lives'''
                LogicMenu.show_interface(background, heroes.get_lives(), generator.number_level)
                pygame.display.flip()


    @staticmethod
    def clear_data(heroes, entities=None, monsters=None, nature=None, during_game=False):
        if entities:
            for e in entities:
                entities.remove(e)
        if nature:
            for n in nature:
                nature.remove(n)
        if monsters:
            for m in monsters:
                monsters.remove(m)
        if not during_game:
            heroes.lst.clear()

    @staticmethod
    def finish_game(background, window, music_file_name):
        pygame.mixer.music.load(music_file_name)
        pygame.mixer.music.play(1, 0)

        while True:
            time.wait(120)
            ViewBackground.fill_view(background, (92, 146, 252))
            ViewBackground.blit_font(background, pygame.font.Font(LogicMenu.font, random.randint(5,10)*10),
                                     u'You are WIN', 1, ((random.randint(0, 255), random.randint(0, 255),
                                                             (random.randint(0, 255)))), random.randint(0, 500),
                                                             random.randint(0, 640))
            for e in pygame.event.get():
                if e.type == QUIT:
                    sys.exit()
                if e.type == KEYDOWN:
                    if e.key==K_ESCAPE:
                        pygame.mixer.music.stop()
                        return
            ViewBackground.blit_view(window, background, 0, 0)
            pygame.display.flip()
