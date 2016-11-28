import pygame
from pygame import *
import threading
import sys
from model.entity.Camera import Camera
from model.entity.LevelGenerator import LevelGenerator
from model.entity.alive.heroes.Hero import Hero
from model.logic.LogicHero import LogicHero
from model.logic.LogicMenu import LogicMenu
from model.logic.LogicMonster import LogicMonster
from view.ViewBackgound import ViewBackground
from model.entity.alive.heroes.Heroes import Heroes


class LogicGame:

    @staticmethod
    def start_game_window(background, background_color, window, timer, during_game=False):

        settings = [119, 97, 100, 102, 105, 106, 108, 59]
        LogicMenu.font='data/coders_crux.ttf'
        LogicMenu.height_menu=70
        LogicMenu.height_game=40
        LogicMenu.background_color=background_color
        LogicMenu.color_active_text=(250, 30, 250)
        LogicMenu.color_simple_text=(250, 250, 30)
        generator = LevelGenerator(platform_width=32, platform_height=32, levels=['levels/level1.txt','levels/level2.txt'],
                                   level='',number_level=0)
        while True:
            choice = LogicMenu.menu(background, window,during_game=False)
            if choice == 1 or choice == 2:

                ''' Creating Heroes'''
                heroes = Heroes()
                hero1 = Hero(x=170, y=170, width=22, height=28, keys=settings[:4], type="hero1",
                             name_image='mario/hero1.png',side=False, power=1, lifes=3, super_hero=False,
                             time_flower_activity=0, time_mushroom_activity=0, left=False, right=False, up=False,
                             on_ground=False, xvel=0, yvel=0, move_speed=4, jump_power=16, gravity=1,
                             fire_ability=False, flower_ability=False)
                heroes.append(hero1)
                if choice == 2:
                    hero2 = Hero(x=270, y=170, width=22, height=28, keys=settings[4:], type="hero2",
                                 name_image='mario/hero2.png',side=False, power=1, lifes=3, super_hero=False,
                                 time_flower_activity=0, time_mushroom_activity=0, left=False, right=False, up=False,
                                 on_ground=False, xvel=0, yvel=0, move_speed=4, jump_power=16, gravity=1,
                                 fire_ability=False, flower_ability=False)
                    heroes.append(hero2)

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

        entities = pygame.sprite.Group()
        for h in heroes.lst:
            entities.add(h)
        nature = pygame.sprite.Group()
        monsters = pygame.sprite.Group()
        platforms = []
        RESULT_LEVEL=[False]

        '''Window Set'''
        generator.generate_level(entities, platforms, monsters, nature)
        level_width = len(generator.level[len(generator.level) - 1]) * generator.platform_width
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

            timer.tick(60)

            '''Creating Threads'''
            t1 = threading.Thread(target=LogicHero.update_hero, args=(heroes, platforms, entities, monsters,RESULT_LEVEL))
            t1.start()
            t2 = threading.Thread(target=LogicMonster.update_monster, args=(monsters, platforms, entities, heroes))
            t2.start()

            '''Set Background'''
            ViewBackground.blit_view(window, background, 0, 0)

            if RESULT_LEVEL[0]:
                heroes.set_default_settings()
                LogicGame.clear_data(heroes,entities,monsters,nature, during_game=True)
                generator.number_level += 1
                LogicGame.start_game(settings, generator, background, window, timer, heroes, during_game=True)
                RESULT_LEVEL[0]=False
                break

            '''Check On Existing Heroes'''
            if heroes.not_exist():
                break

            '''Centering Camera'''
            camera.in_center(heroes.set_last_hero().rect)

            '''Draw objects'''
            for n in nature:
                value = camera.shift_object(n.rect)
                ViewBackground.blit_view(window, n.image, value.x, value.y)
            for entity in entities:
                value = camera.shift_object(entity.rect)
                ViewBackground.blit_view(window, entity.image, value.x, value.y)

            '''Update Background'''
            ViewBackground.fill_view(background, LogicMenu.background_color)

            '''Show lives'''
            LogicMenu.show_lives(background, heroes)

            pygame.display.update()

    @staticmethod
    def clear_data(heroes,entities,monsters,nature,during_game=False):
        for e in entities:
            entities.remove(e)
        for n in nature:
            nature.remove(n)
        for m in monsters:
            monsters.remove(m)
        if not during_game:
            heroes.lst.clear()
