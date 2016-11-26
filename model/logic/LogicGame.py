import pygame
import threading
import sys,time
from model.entity.Camera import Camera
from model.entity.Level import Level
from model.entity.alive.heroes.Hero import Hero
from model.logic.LogicCamera import LogicCamera
from model.logic.LogicHero import LogicHero
from model.logic.LogicMenu import LogicMenu
from model.logic.LogicMonster import LogicMonster
from view.ViewBackgound import View
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

        while True:

            choice = LogicMenu.menu(background, window,during_game=False)
            if choice == 1 or choice == 2:

                '''Creating Heroes'''
                entities = pygame.sprite.Group()
                nature = pygame.sprite.Group()
                monsters = pygame.sprite.Group()
                platforms = []
                heroes = Heroes()
                hero1 = Hero(x=170, y=170, width=22, height=28, keys=settings[:4], type="hero1",
                             name_image='mario/hero1.png',side=False, power=1, lifes=3, super_hero=False,
                             time_flower_activity=0, time_mushroom_activity=0, left=False, right=False, up=False, on_ground=False, xvel=0, yvel=0,
                             move_speed=4, jump_power=16, gravity=1, fire_ability=False, flower_ability=False)
                heroes.append(hero1)
                entities.add(hero1)
                if choice == 2:
                    hero2 = Hero(x=270, y=170, width=22, height=28, keys=settings[4:], type="hero2",
                                 name_image='mario/hero2.png',side=False, power=1, lifes=3, super_hero=False,
                                 time_flower_activity=0, time_mushroom_activity=0, left=False, right=False, up=False, on_ground=False, xvel=0,
                                 yvel=0, move_speed=4, jump_power=16, gravity=1, fire_ability=False, flower_ability=False)
                    heroes.append(hero2)
                    entities.add(hero2)

                '''Window Set'''
                Level.show(entities, platforms, monsters, nature)
                level_width = len(Level.level[len(Level.level) - 1]) * Level.platform_width()
                level_height = len(Level.level) * Level.platform_height()
                camera = Camera(level_width, level_height)

                '''Start GAME'''
                LogicGame.start_game(settings, background, window, timer, heroes, entities, monsters,
                                     platforms, nature, camera, during_game=True)

            if choice == 3:

                ''' Move to settings'''
                if not during_game:
                    LogicMenu.settings(background, window, settings, during_game)
                    View.fill_view(background, background_color)

            if choice == 4:

                ''' Exit Game'''
                sys.exit()

    @staticmethod
    def start_game(settings, background,  window, timer, heroes, entities, monsters, platforms, nature,
                  camera, during_game=True):

        while True:

            timer.tick(60)
            button = LogicHero.check_press_key(heroes, entities, platforms, monsters)

            '''Show Menu During Game'''
            if button:
                choice = LogicMenu.menu(background,  window, during_game=True)

                if choice == 1:

                    ''' Move To Settings During Game'''
                    LogicMenu.settings(background,  window, settings,during_game=True)
                    heroes.update_keys(settings)
                    View.fill_view(background, LogicMenu.background_color)

                if choice == 3:

                    ''' Finish Existing Game'''
                    if during_game:
                        LogicGame.clear_data(heroes,entities,monsters,nature)
                        break

                if choice == 4:

                    ''' Exit Game'''
                    sys.exit()

            '''Creating Threads'''
            t1 = threading.Thread(target=LogicHero.update_hero, args=(heroes, platforms, entities, monsters))
            t1.start()
            t2 = threading.Thread(target=LogicMonster.update_monster, args=(monsters, platforms, entities, heroes))
            t2.start()

            '''Set Background'''
            View.blit_view(window, background, 0, 0)

            '''Check On Exist Heroes'''
            if heroes.not_exist():
                break

            '''Centering Camera'''
            LogicCamera.in_center(camera, heroes.set_last_hero())

            '''Draw objects'''
            for n in nature:
                value = camera.shift_object(n)
                View.blit_view(window, n.image, value.x, value.y)
            for entity in entities:
                value = camera.shift_object(entity)
                View.blit_view(window, entity.image, value.x, value.y)

            '''Update Background'''
            View.fill_view(background, LogicMenu.background_color)

            '''Show lives'''
            LogicMenu.show_lives(background, heroes)

            pygame.display.update()

    @staticmethod
    def clear_data(heroes,entities,monsters,nature):
        for e in entities:
            entities.remove(e)
        for n in nature:
            nature.remove(n)
        for m in monsters:
            monsters.remove(m)
        heroes.lst.clear()
