from model.entity.alive.enemies.Bowser import Bowser

from model.entity.alive.enemies.Slub import Slub
from model.entity.dead.BonusBlock import BonusBlock
from model.entity.dead.Ground import Ground
from model.entity.dead.Nature import Nature
from model.entity.dead.SimpleBlock import SimpleBlock


class Level:

    PLATFORM_WIDTH = 32
    PLATFORM_HEIGHT = 32
    level = []
    @staticmethod
    def show(entities, platforms, monsters, nature):
        x = y = 0
        Level.level = open('levels/levels.txt').readlines()
        for row in range(len(Level.level)):
            Level.level[row] = Level.level[row].replace('\n', '')
            Level.level[row] = Level.level[row].replace('\t', '    ')

        for row in Level.level:
            for symbol in row:
                if symbol == "0":
                    item = Nature(x=x, y=y, width=64, height=48, image='blocks/cloud.png')
                    nature.add(item)
                if symbol == "1":
                    item = Nature(x=x, y=y, width=128, height=32, image='blocks/bush-1.png')
                    nature.add(item)
                if symbol == "2":
                    item = Nature(x=x, y=y, width=96, height=32, image='blocks/bush-2.png')
                    nature.add(item)
                if symbol == "3":
                    item = Nature(x=x, y=y, width=64, height=32, image='blocks/bush-3.png')
                    nature.add(item)
                if symbol == "4":
                    item = Ground(x=x, y=y, width=64, height=64, image='blocks/pipe_greensmall.png')
                    entities.add(item)
                    platforms.append(item)
                if symbol == "5":
                    item = Ground(x=x, y=y, width=64, height=96, image='blocks/pipe_green.png')
                    entities.add(item)
                    platforms.append(item)
                if symbol == "6":
                    item = Ground(x=x, y=y, width=64, height=128, image='blocks/pipe_greenbig.png')
                    entities.add(item)
                    platforms.append(item)


                if symbol == "-":
                    item = SimpleBlock(x=x, y=y,width=Level.PLATFORM_WIDTH, height=Level.PLATFORM_HEIGHT,
                                       image='blocks/block_2.png', image_damage='blocks/block_1.png')
                    entities.add(item)
                    platforms.append(item)
                if symbol == ".":
                    item = Ground(x=x, y=y, width=Level.PLATFORM_WIDTH, height=Level.PLATFORM_HEIGHT,
                                  image='blocks/platform.jpg')
                    entities.add(item)
                    platforms.append(item)
                if symbol == "?":
                    item = BonusBlock(x=x, y=y, width=Level.PLATFORM_WIDTH, height=Level.PLATFORM_HEIGHT,
                                      images=['blocks/bonus_block_active_1.png', 'blocks/bonus_block_active_2.png'],
                                      image_simple='blocks/bonus_block_simple.png',
                                      koef=20, activity=True,
                                      change_ability=True, type_bonus=1)
                    entities.add(item)
                    platforms.append(item)
                if symbol == "s":
                    item = Slub(x=x, y=y, width=Level.PLATFORM_WIDTH, height=Level.PLATFORM_HEIGHT,
                                images_existing=['enemies/simple_enemy/slub1.png',
                                                 'enemies/simple_enemy/slub2.png'],
                                image_killed='enemies/simple_enemy/slub3.png',
                                koef=49)
                    monsters.add(item)
                    entities.add(item)
                    platforms.append(item)
                if symbol == "b":
                    item = Bowser(x=x, y=y, width=48, height=48, images_existing=[['enemies/bowser/bowser1_left.png',
                                                                                   'enemies/bowser/bowser2_left.png'],
                                                                                   ['enemies/bowser/bowser1_right.png',
                                                                                   'enemies/bowser/bowser2_right.png']],
                                                                 image_killed=['enemies/bowser/bowser1_left_die.png',
                                                                               'enemies/bowser/bowser1_right_die.png'],
                                  koef=9, side=True)
                    monsters.add(item)
                    entities.add(item)
                    platforms.append(item)
                x += Level.PLATFORM_WIDTH
            y += Level.PLATFORM_HEIGHT
            x = 0
