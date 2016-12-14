import pygame
import sys
from pygame import *
from model.entity.alive.Fire import Fire
from model.entity.alive.enemies.Bowser import Bowser
from model.entity.alive.enemies.Monster import Monster
from model.entity.alive.enemies.BlueFlower import BlueFlower
from model.entity.alive.enemies.Slub import Slub
from model.entity.alive.heroes.Hero import Hero
from model.entity.dead.BonusBlock import BonusBlock
from model.entity.dead.Flower import Flower
from model.entity.dead.Mushroom import Mushroom
from model.entity.dead.Bonus import Bonus
from model.entity.dead.Exit import Exit
from model.entity.dead.SimpleBlock import SimpleBlock


class LogicHero:

    @staticmethod
    def check_press_key(heroes, entities, monsters):
        for e in pygame.event.get():
            for hero in heroes.lst:
                if e.type == QUIT:
                    sys.exit()
                if e.type == KEYDOWN:
                    if e.key == hero.key_fire and hero.fire_ability:
                        LogicHero.create_fire(hero, entities, monsters)
                    if e.key == hero.key_left:
                        hero.left = True
                        hero.side = True
                    if e.key == hero.key_right:
                        hero.right = True
                        hero.side = False
                    if e.key == hero.key_up:
                        hero.up = True
                    if e.key == K_ESCAPE:
                        return True
                if e.type == KEYUP:
                    if e.key == hero.key_right:
                        hero.right = False
                    if e.key == hero.key_left:
                        hero.left = False
                    if e.key == hero.key_up:
                        hero.up = False

    @staticmethod
    def update_heroes(heroes, blocks, entities, monsters, RESULT):
        if not heroes.not_exist():

            for block in blocks:
                if isinstance(block, BonusBlock):
                    if block.change_ability:
                            block.change_image()
                if isinstance(block, Bonus):
                    if block.amount_images_appearing != 0:
                        block.appear_bonus()
                    else:
                        block.exist_bonus()

            for hero in heroes.lst:
                hero.update()

                hero.rect.y += hero.yvel
                if hero.rect.y >= 640:
                    hero.lifes -= 1
                    heroes.killed(hero, entities)
                    heroes.move_to_start()
                    break

                status_hero = LogicHero.contact_with_blocks(heroes, hero, 0, hero.yvel, blocks, entities, monsters)
                if status_hero == True:
                    RESULT[0] = True
                    return

                hero.rect.x += hero.xvel
                status_hero = LogicHero.contact_with_blocks(heroes, hero, hero.xvel, 0, blocks, entities, monsters)

                if status_hero == True:
                    RESULT[0] = True
                    return
        # print(time.time())

    @staticmethod
    def contact_with_blocks(heroes, hero, xvel, yvel, blocks, entities, monsters):
        if not heroes.not_exist():

            for block in blocks:
                hero.update_bonus()
                if sprite.collide_rect(hero, block):
                    if xvel > 0:
                        hero.rect.right = block.rect.left
                        if isinstance(block, Monster) and block.alive:
                            hero.lifes -= 1
                            heroes.killed(hero, entities)
                            return False
                        elif isinstance(block, Bonus):
                            LogicHero.contact_bonus(hero, block, blocks, entities)
                            LogicHero.contact_with_blocks(heroes, hero, xvel, yvel, blocks, entities, monsters)
                            return
                    elif xvel < 0:
                        hero.rect.left = block.rect.right
                        if isinstance(block, Monster) and block.alive:
                            hero.lifes -= 1
                            heroes.killed(hero, entities)
                            return False
                        elif isinstance(block, Bonus):
                            LogicHero.contact_bonus(hero, block, blocks, entities)
                            LogicHero.contact_with_blocks(heroes, hero, xvel, yvel, blocks, entities, monsters)
                            return
                    if yvel > 0:
                        hero.rect.bottom = block.rect.top
                        hero.on_ground = True
                        hero.yvel = 0
                        if (isinstance(block, Bowser) or isinstance(block, BlueFlower)) and block.alive:
                            hero.lifes -= 1
                            heroes.killed(hero, entities)
                            return False
                        elif isinstance(block, Slub) and block.alive:
                            block.alive = False
                            block.lifes -=hero.power
                            block.killed(monsters, entities, blocks)
                            LogicHero.contact_with_blocks(heroes, hero, xvel, yvel, blocks, entities, monsters)
                            return
                        elif isinstance(block, Bonus):
                            LogicHero.contact_bonus(hero, block, blocks, entities)
                            LogicHero.contact_with_blocks(heroes, hero, xvel, yvel, blocks, entities, monsters)
                            return
                    elif yvel < 0:
                        hero.rect.top = block.rect.bottom
                        hero.yvel = 0
                        if isinstance(block, Monster) and block.alive:
                            hero.lifes -= 1
                            heroes.killed(hero, entities)
                            return False
                        elif isinstance(block, SimpleBlock):
                            block.lifes -=hero.power
                            block.killed(blocks, entities)
                            LogicHero.contact_with_blocks(heroes, hero, xvel, yvel, blocks, entities, monsters)
                            return
                        elif isinstance(block, BonusBlock) and block.activity:
                            LogicHero.contact_bonus_blocks(blocks,block, entities)
                            LogicHero.contact_with_blocks(heroes, hero, xvel, yvel, blocks, entities, monsters)
                            return
                        LogicHero.contact_bonus(hero, block, blocks, entities)
                        LogicHero.contact_with_blocks(heroes, hero, xvel, yvel, blocks, entities, monsters)
                        return
                    if isinstance(block, Exit):
                        time.wait(200)
                        return True
            return False

    @staticmethod
    def contact_bonus(hero, block, blocks, entities):
      if isinstance(block, Bonus):
        if isinstance(block, Mushroom):
            hero.time_mushroom_activity += block.time_activity
            hero.fire_ability = True
        if isinstance(block, Flower):
            hero.get_super_jump(block.flower_value)
            hero.time_flower_activity += block.time_activity
            hero.flower_ability = True
        entities.remove(block)
        blocks.remove(block)

    @staticmethod
    def contact_bonus_blocks(blocks, block, entities):
        if isinstance(block, BonusBlock):
            block.make_simple()
            bonus = None
            if block.type_bonus == 1:
                bonus = Flower(x=block.x + 3, y=block.y - 59, width=26, height=27,
                               start_image='data/flower_1.png',
                               images_appearing=['data/flower_27.png', 'data/flower_25.png', 'data/flower_23.png',
                                                 'data/flower_21.png', 'data/flower_19.png', 'data/flower_17.png',
                                                 'data/flower_15.png', 'data/flower_13.png', 'data/flower_11.png',
                                                 'data/flower_9.png',  'data/flower_7.png', 'data/flower_5.png',
                                                 'data/flower_3.png',  'data/flower_1.png'],
                               images_existing=['data/flower_exist_day_1.png', 'data/flower_exist_day_2.png',
                                                'data/flower_exist_day_3.png', 'data/flower_exist_day_4.png'],
                               koef=30, time_activity=200000, flower_value=1.2, change_ability=True)
            if block.type_bonus == 2:
                bonus = Mushroom(x=block.x + 3, y=block.y - 59, width=26, height=27,
                                 start_image='data/mushroom_1.png',
                                 images_appearing=['data/mushroom_27.png', 'data/mushroom_25.png', 'data/mushroom_23.png',
                                                   'data/mushroom_21.png', 'data/mushroom_19.png', 'data/mushroom_17.png',
                                                   'data/mushroom_15.png', 'data/mushroom_13.png', 'data/mushroom_11.png',
                                                   'data/mushroom_9.png', 'data/mushroom_7.png', 'data/mushroom_5.png',
                                                   'data/mushroom_3.png', 'data/mushroom_1.png'],
                                 images_existing=['data/mushroom_exist_day_1.png',
                                                  'data/mushroom_exist_day_2.png'],
                                 koef=30, time_activity=200000, change_ability=True)
            if bonus:
                blocks.append(bonus)
                entities.add(bonus)

    @staticmethod
    def create_fire(hero, entities, monsters):
        if isinstance(hero, Hero):
            if hero.side:
                fireball = Fire(x=hero.rect.x-10, y=hero.rect.y+(hero.height//2), width=7, height=6,
                                image='data/fireball.png', side=hero.side, power=1, xvel=0, yvel=0, gravity=1,
                                move_speed=5, left=True, right=False, up=False, on_ground=False, max_way=96, alive=True)
            else:
                fireball = Fire(x=hero.rect.x+hero.width, y=hero.rect.y + (hero.height // 2), width=7, height=6,
                                image='data/fireball.png', side=hero.side, power=1, xvel=0, yvel=0, gravity=1,
                                move_speed=5, left=True, right=False, up=False, on_ground=False, max_way=96, alive=True)
            entities.add(fireball)
            monsters.add(fireball)
