import threading

import pygame
from model.entity.alive.heroes.Heroes import Heroes
from pygame import *

from model.entity.Camera import Camera
from model.entity.Level import Level
from model.entity.Live import Live
from model.entity.alive.heroes.Hero import Hero
from model.logic.LogicCamera import LogicCamera
from model.logic.LogicHero import LogicHero
from model.logic.LogicMenu import LogicMenu
from model.logic.LogicMonster import LogicMonster
from view.ViewBackgound import View

win_width = 800
win_height = 640
background_color = (92, 146, 252)


def main():
    pygame.init()

    window = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption("Mario")
    background = Surface((win_width, win_height))
    View.fill_view(background, background_color)


    while True:
        settings = [119, 97, 100, 102, 105, 106, 108, 59]
        choice = LogicMenu.menu(background, window, settings)

        if choice == 1 or choice == 2:
            entities = pygame.sprite.Group()
            nature = pygame.sprite.Group()
            monsters = pygame.sprite.Group()
            platforms = []
            timer = pygame.time.Clock()
            heroes = Heroes()

            hero1 = Hero(x=170, y=170, width=22, height=28, keys=settings[:4], type="hero1",name_image='mario/hero1.png')
            heroes.append(hero1)
            entities.add(hero1)
            if choice == 2:
                hero2 = Hero(x=270, y=170, width=22, height=28, keys=settings[4:], type="hero2", name_image='mario/hero2.png')
                heroes.append(hero2)
                entities.add(hero2)

            live = Live(x=win_width//2, y=0, width=50, height=100, name_image='mario/hero1.png')
            entities.add(live)
            background = Surface((win_width, win_height))
            View.fill_view(background, background_color)
            Level.show(entities, platforms, monsters, nature)
            level_width = len(Level.level[len(Level.level)-1]) * Level.PLATFORM_WIDTH
            level_height = len(Level.level) * Level.PLATFORM_HEIGHT
            camera = Camera(level_width, level_height)
            while True:
                timer.tick(60)

                button = LogicHero.check_press_key(heroes, entities, platforms, monsters)

                if button:

                    if LogicMenu.during_game_menu(background, window, heroes) == 3:
                        break
                View.fill_view(background, background_color)

                # LogicMonster.update_monster(monsters, platforms, entities, heroes)
                # LogicHero.update_hero(heroes, platforms, entities, monsters)
                t1 = threading.Thread(target=LogicHero.update_hero, args=(heroes, platforms, entities, monsters))
                t1.start()
                t2 = threading.Thread(target=LogicMonster.update_monster, args=(monsters, platforms, entities, heroes))
                t2.start()

                View.blit_view(window, background, 0, 0)

                if heroes.exist():
                    break
                else:
                    LogicCamera.in_center(camera, heroes.set_last_hero())

                for n in nature:
                    value = camera.shift_object(n)
                    View.blit_view(window, n.image, value.x, value.y)
                for entity in entities:
                    value = camera.shift_object(entity)
                    View.blit_view(window, entity.image, value.x, value.y)
                pygame.display.update()

if __name__ == "__main__":
    main()
