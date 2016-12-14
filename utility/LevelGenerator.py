from model.entity.alive.enemies.Bowser import Bowser
from model.entity.alive.enemies.Slub import Slub
from model.entity.dead.BonusBlock import BonusBlock
from model.entity.dead.Ground import Ground
from model.entity.dead.Nature import Nature
from model.entity.dead.Exit import Exit
from model.entity.dead.SimpleBlock import SimpleBlock
from model.entity.alive.enemies.BlueFlower import BlueFlower


class LevelGenerator:

    def __init__(self, platform_width=0, platform_height=0, levels=[], level='', number_level=0):
        self.__platform_width = platform_width
        self.__platform_height = platform_height
        self.__levels = levels
        self.__level = level
        self.__number_level = number_level
        self.__max_level = len(levels)

    @property
    def platform_width(self):
        return self.__platform_width

    @property
    def platform_height(self):
        return self.__platform_height

    @property
    def levels(self):
        return self.__levels

    @levels.setter
    def levels(self, value):
        self.__levels = value

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        self.__level = value

    @property
    def max_level(self):
        return self.__max_level

    @property
    def number_level(self):
        return self.__number_level

    @number_level.setter
    def number_level(self, value):
        self.__number_level += value

    def get_levels(self, index):
        return self.levels[index]

    def generate_level(self, entities, platforms, monsters, nature):
        x = y = 0
        self.level = open(self.get_levels(self.number_level)).readlines()
        for row in range(len(self.level)):
            self.level[row] = self.level[row].replace('\n', '')
            self.level[row] = self.level[row].replace('\t', '    ')
        for row in self.level:
            for symbol in row:
                if symbol == "." or symbol == "#":
                    item = Ground(x=x, y=y, width=self.platform_width, height=self.platform_height,
                                  image='data/platform.jpg')
                    entities.add(item)
                    platforms.append(item)
                elif symbol == "4":
                    item = Ground(x=x, y=y, width=64, height=64, image='data/pipe_greensmall.png')
                    entities.add(item)
                    platforms.append(item)
                elif symbol == "5":
                    item = Ground(x=x, y=y, width=64, height=96, image='data/pipe_green.png')
                    entities.add(item)
                    platforms.append(item)
                elif symbol == "6":
                    item = Ground(x=x, y=y, width=64, height=128, image='data/pipe_greenbig.png')
                    entities.add(item)
                    platforms.append(item)
                elif symbol == "-":
                    item = SimpleBlock(x=x, y=y, width=self.platform_width, height=self.platform_height,
                                       image='data/block_2.png', image_damage='data/block_1.png', lifes=2)
                    entities.add(item)
                    platforms.append(item)
                elif symbol == "f":
                    item = BonusBlock(x=x, y=y, width=self.platform_height, height=self.platform_height,
                                      images_existing=['data/bonus_block_active_1.png',
                                                       'data/bonus_block_active_2.png'],

                                      image_simple='data/bonus_block_simple.png', koef=20, activity=True,
                                      change_ability=True, type_bonus=1)
                    entities.add(item)
                    platforms.append(item)
                elif symbol == "m":
                    item = BonusBlock(x=x, y=y, width=self.platform_height, height=self.platform_height,
                                      images_existing=['data/bonus_block_active_1.png',
                                                       'data/bonus_block_active_2.png'],
                                      image_simple='data/bonus_block_simple.png', koef=20, activity=True,
                                      change_ability=True, type_bonus=2)
                    entities.add(item)
                    platforms.append(item)
                elif symbol == "s":
                    item = Slub(x=x, y=y, width=self.platform_height, height=self.platform_height,
                                images_existing=['data/slub1.png',
                                                 'data/slub2.png'],
                                image_killed='data/slub3.png', koef=49, lifes=1, max_way=96, xvel=0,
                                yvel=0, gravity=1, move_speed=1, left=True, right=False, up=False, on_ground=False,
                                alive=True)
                    monsters.add(item)
                    entities.add(item)
                    platforms.append(item)
                elif symbol == "F":
                    item = BlueFlower(x=x+self.platform_width//2, y=y, width=32, height=32,
                                  images_existing=['data/blueflower1.png',
                                                   'data/blueflower2.png'],
                                  image_killed='data/blueflower_killed.png',
                                  koef=15, koef_exist=2,lifes=1, max_way=96, on_ground=True, alive=True, moving=True)
                    monsters.add(item)
                    entities.add(item)
                    platforms.append(item)
                elif symbol == "b":
                    item = Bowser(x=x, y=y, width=48, height=48,
                                  images_existing=[['data/bowser1_left.png',
                                                    'data/bowser2_left.png'],
                                                   ['data/bowser1_right.png',
                                                    'data/bowser2_right.png']],
                                  image_killed=['data/bowser1_left_die.png',
                                                'data/bowser1_right_die.png'], koef=9, side=True, lifes=5,
                                  max_way=96, xvel=0, yvel=0, gravity=1, move_speed=1, left=True, right=False, up=False,
                                  on_ground=False, alive=True)
                    monsters.add(item)
                    entities.add(item)
                    platforms.append(item)
                elif symbol == "K":
                    item = Exit(x=x, y=y, width=96, height=192, image='data/castle_right.png')
                    entities.add(item)
                    platforms.append(item)
                elif symbol == "k":
                    item = Nature(x=x, y=y, width=96, height=192, image='data/castle_left.png')
                    nature.add(item)
                elif symbol == "E":
                    item = Exit(x=x, y=y-8, width=132, height=20, image='data/pipe_exit_2.png')
                    entities.add(item)
                    platforms.append(item)
                elif symbol == "e":
                    item = Ground(x=x, y=y+4, width=132, height=44, image='data/pipe_exit_1.png')
                    nature.add(item)
                elif symbol == "0":
                    item = Nature(x=x, y=y, width=64, height=48, image='data/cloud.png')
                    nature.add(item)
                elif symbol == "1":
                    item = Nature(x=x, y=y, width=128, height=32, image='data/bush-1.png')
                    nature.add(item)
                elif symbol == "2":
                    item = Nature(x=x, y=y, width=96, height=32, image='data/bush-2.png')
                    nature.add(item)
                elif symbol == "3":
                    item = Nature(x=x, y=y, width=64, height=32, image='data/bush-3.png')
                    nature.add(item)
                x += self.platform_height
            y += self.platform_height
            x = 0
        self.number_level = +1
