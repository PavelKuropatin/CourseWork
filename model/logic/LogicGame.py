import pygame
import threading
import sys
from model.entity.Camera import Camera
from model.entity.Level import Level
from model.entity.Live import Live
from model.entity.alive.heroes.Hero import Hero
from model.logic.LogicCamera import LogicCamera
from model.logic.LogicHero import LogicHero
from model.logic.LogicMenu import LogicMenu
from model.logic.LogicMonster import LogicMonster
from view.ViewBackgound import View
from model.entity.alive.heroes.Heroes import Heroes


class LogicGame:

    @staticmethod
    def startGameWindow(settings, background, background_color, window, timer):

        while True:
            choice = LogicMenu.menu(background, window)
            if choice == 1 or choice == 2:
                entities = pygame.sprite.Group()
                nature = pygame.sprite.Group()
                monsters = pygame.sprite.Group()
                platforms = []
                heroes = Heroes()

                hero1 = Hero(x=170, y=170, width=22, height=28, keys=settings[:4], type="hero1",
                             name_image='mario/hero1.png')
                heroes.append(hero1)
                entities.add(hero1)

                if choice == 2:
                    hero2 = Hero(x=270, y=170, width=22, height=28, keys=settings[4:], type="hero2",
                                 name_image='mario/hero2.png')
                    heroes.append(hero2)
                    entities.add(hero2)

                live = Live(x=background.get_width() // 2, y=0, width=50, height=100, name_image='mario/hero1.png')
                entities.add(live)

                Level.show(entities, platforms, monsters, nature)
                level_width = len(Level.level[len(Level.level) - 1]) * Level.PLATFORM_WIDTH
                level_height = len(Level.level) * Level.PLATFORM_HEIGHT
                camera = Camera(level_width, level_height)

                LogicGame.startGame(settings, background, background_color, window, timer, heroes, entities, monsters,
                                    platforms, nature, camera)

            if choice == 3:
                LogicMenu.settings(background, window, settings)
                View.fill_view(background, (0, 100, 200))

            if choice == 4:
                sys.exit()

    @staticmethod
    def startGame(settings,background, background_color, window, timer, heroes, entities, monsters,
                                          platforms, nature, camera):
        while True:

            timer.tick(60)
            button = LogicHero.check_press_key(heroes, entities, platforms, monsters)

            if button:
                choice = LogicMenu.during_game_menu(background, window, heroes)
                if choice == 1:
                    LogicMenu.settings_during_game(background, window, heroes)
                    View.fill_view(background, (0, 100, 200))
                if choice == 3:
                    LogicMenu.update_settings(heroes, settings)
                    break
                if choice == 4:
                    sys.exit()

            View.fill_view(background, background_color)

            t1 = threading.Thread(target=LogicHero.update_hero, args=(heroes, platforms, entities, monsters))
            t1.start()
            t2 = threading.Thread(target=LogicMonster.update_monster, args=(monsters, platforms, entities, heroes))
            t2.start()

            View.blit_view(window, background, 0, 0)

            if heroes.not_exist():
                break

            LogicCamera.in_center(camera, heroes.set_last_hero())

            for n in nature:
                value = camera.shift_object(n)
                View.blit_view(window, n.image, value.x, value.y)
            for entity in entities:
                value = camera.shift_object(entity)
                View.blit_view(window, entity.image, value.x, value.y)
            pygame.display.update()

