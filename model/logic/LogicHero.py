import pygame,sys
from pygame import *

from model.entity.alive.Fire import Fire
from model.entity.alive.enemies.Bowser import Bowser
from model.entity.alive.enemies.Monster import Monster
from model.entity.alive.enemies.Slub import Slub
from model.entity.alive.heroes.Hero import Hero
from model.entity.dead.BonusBlock import BonusBlock
from model.entity.dead.Flower import Flower
from model.entity.dead.SimpleBlock import SimpleBlock


class LogicHero:

    @staticmethod
    def check_press_key(heroes, entities, blocks, monsters):
        for e in pygame.event.get():
            for hero in heroes.lst:
                if e.type == QUIT:
                    sys.exit()
                if e.type == KEYDOWN:
                    if e.key == hero.key_fire:
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
    def update_hero(heroes, blocks, entities, monsters):
        if not heroes.not_exist():
            for block in blocks:
                if isinstance(block, BonusBlock):
                    if block.change_ability:
                            block.change_image()
                if isinstance(block, Flower):
                    if block.amount_images_appearing != 0:
                        block.appear_flower()
                    else:
                        block.exist_flower()
            for hero in heroes.lst:
                if hero.up:
                    if hero.on_ground:
                        hero.yvel = -hero.jump_power
                if hero.left:
                    hero.xvel = -hero.move_speed
                if hero.right:
                    hero.xvel = hero.move_speed
                if not (hero.left or hero.right):
                    hero.xvel = 0
                if not hero.on_ground:
                    hero.yvel += hero.gravity
                hero.on_ground = False
                hero.rect.y += hero.yvel
                if hero.rect.y >= 640:
                    heroes.killed(hero, entities)
                    hero.move_to_start()
                    break
                if LogicHero.contact_with_blocks(heroes, hero, 0, hero.yvel, blocks, entities, monsters):
                    break
                hero.rect.x += hero.xvel
                if LogicHero.contact_with_blocks(heroes, hero, hero.xvel, 0, blocks, entities, monsters):
                    break

        else:
            return

    @staticmethod
    def contact_with_blocks(heroes, hero, xvel, yvel, blocks, entities, monsters):
        if not heroes.not_exist():
            for block in blocks:

                if isinstance(hero, Hero) and hero.super_hero:

                    if hero.time_flower_activity == 0:
                        hero.get_simple_sump()

                    hero.time_activity = -1

                if sprite.collide_rect(hero, block):

                    if xvel > 0:
                        hero.rect.right = block.rect.left
                        if isinstance(block, Monster) and block.changing:
                                heroes.killed(hero, entities)
                                return True

                        if isinstance(block, Flower) and block.activity:
                            LogicHero.contact_flower(hero, block, blocks, entities)
                            LogicHero.contact_with_blocks(heroes, hero, xvel, yvel, blocks, entities, monsters)
                            break

                    if xvel < 0:

                        hero.rect.left = block.rect.right

                        if isinstance(block, Monster) and block.changing:

                                heroes.killed(hero, entities)
                                return True

                        if isinstance(block, Flower) and block.activity:
                            LogicHero.contact_flower(hero, block, blocks, entities)
                            LogicHero.contact_with_blocks(heroes, hero, xvel, yvel, blocks, entities, monsters)
                            break

                    if yvel > 0:

                        hero.rect.bottom = block.rect.top
                        hero.on_ground = True
                        hero.yvel = 0

                        if isinstance(block, Bowser) and block.changing:
                            heroes.killed(hero, entities)
                            return True

                        if isinstance(block, Slub) and block.changing:
                            block.changing = False
                            block.lifes = -hero.power
                            block.killed(monsters, entities, blocks)
                            LogicHero.contact_with_blocks(heroes, hero, xvel, yvel, blocks, entities, monsters)
                            break

                        if isinstance(block, Flower) and block.activity:
                            LogicHero.contact_flower(hero, block, blocks, entities)
                            LogicHero.contact_with_blocks(heroes, hero, xvel, yvel, blocks, entities, monsters)
                            break

                    if yvel < 0:

                        hero.rect.top = block.rect.bottom
                        hero.yvel = 0

                        if isinstance(block, Monster) and block.changing:
                            heroes.killed(hero, entities)
                            return True

                        if isinstance(block, SimpleBlock):
                            block.decrease_block_lives(hero.power, block, blocks, entities)
                            LogicHero.contact_with_blocks(heroes, hero, xvel, yvel, blocks, entities, monsters)
                            break

                        if isinstance(block, BonusBlock) and block.activity:

                            LogicHero.contact_bonus_blocks(blocks,block, entities)
                            LogicHero.contact_with_blocks(heroes, hero, xvel, yvel, blocks, entities, monsters)
                            break

                        LogicHero.contact_flower(hero, block, blocks, entities)
                        LogicHero.contact_with_blocks(heroes, hero, xvel, yvel, blocks, entities, monsters)
                        break
        # return False

    @staticmethod
    def contact_flower(hero, block, blocks, entities):

        if isinstance(block, Flower):
            hero.get_super_jump(1.2, block.time_activity)
            block.activity = False
            entities.remove(block)
            blocks.remove(block)

    @staticmethod
    def contact_bonus_blocks(blocks, block, entities):

        if isinstance(block, BonusBlock):
            block.make_simple()
            bonus = None
            if block.type_bonus == 1:
                bonus = Flower(x=block.x + 3, y=block.y - 59, width=26, height=27,
                               start_image='blocks/flower_appear/flower_1.png',
                               images_appearing=['blocks/flower_appear/flower_27.png',
                                         'blocks/flower_appear/flower_25.png',
                                         'blocks/flower_appear/flower_23.png',
                                         'blocks/flower_appear/flower_21.png',
                                         'blocks/flower_appear/flower_19.png',
                                         'blocks/flower_appear/flower_17.png',
                                         'blocks/flower_appear/flower_15.png',
                                         'blocks/flower_appear/flower_13.png',
                                         'blocks/flower_appear/flower_11.png',
                                         'blocks/flower_appear/flower_9.png',
                                         'blocks/flower_appear/flower_7.png',
                                         'blocks/flower_appear/flower_5.png',
                                         'blocks/flower_appear/flower_3.png',
                                         'blocks/flower_appear/flower_1.png'],
                               images_existing=['blocks/flower_exist_day/flower_1.png',
                                        'blocks/flower_exist_day/flower_2.png',
                                        'blocks/flower_exist_day/flower_3.png',
                                        'blocks/flower_exist_day/flower_4.png'],
                               time_activity=250000)
            if bonus:
                blocks.append(bonus)
                entities.add(bonus)

    @staticmethod
    def create_fire(hero, entities, monsters):
        if isinstance(hero, Hero):
            if hero.side:
                fireball = Fire(x=hero.rect.x-10, y=hero.rect.y+(hero.height//2), width=7, height=6, image='blocks/fireball.png', side=hero.side)

            else:
                fireball = Fire(x=hero.rect.x+hero.width, y=hero.rect.y + (hero.height // 2), width=7, height=6,
                                image= 'blocks/fireball.png',
                                side=hero.side)
            entities.add(fireball)
            monsters.add(fireball)
