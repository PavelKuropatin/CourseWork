from model.entity.alive.enemies.Bowser import Bowser
from model.entity.alive.enemies.Slub import Slub
from model.entity.dead.BonusBlock import BonusBlock
from model.entity.dead.Ground import Ground
from model.entity.dead.Nature import Nature
from model.entity.dead.Castle import Castle
from model.entity.dead.SimpleBlock import SimpleBlock


class LevelGenerator:

    def __init__(self, platform_width=0, platform_height=0, levels=[], level='',number_level=0):
        self.__platform_width = platform_width
        self.__platform_height = platform_height
        self.__levels = levels
        self.__level = level
        self.__number_level = number_level

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
    def number_level(self):
        return self.__number_level
    @number_level.setter
    def number_level(self, value):
        self.__number_level += value

    def get_levels(self,index):
        return self.levels[index]

    def generate_level(self,entities, platforms, monsters, nature):
        x = y = 0
        self.level = open(self.get_levels(self.number_level)).readlines()
        for row in range(len(self.level)):
            self.level[row] = self.level[row].replace('\n', '')
            self.level[row] = self.level[row].replace('\t', '    ')
        for row in self.level:
            for symbol in row:
                if symbol == "K":
                    item = Castle(x=x, y=y, width=96, height=192, image='blocks/castle_right.png')
                    entities.add(item)
                    platforms.append(item)
                if symbol == "k":
                    item = Castle(x=x, y=y, width=196, height=192, image='blocks/castle_left.png')
                    nature.add(item)
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
                    item = SimpleBlock(x=x, y=y,width=self.platform_width, height=self.platform_height,
                                       image='blocks/block_2.png', image_damage='blocks/block_1.png', lifes=2)
                    entities.add(item)
                    platforms.append(item)
                if symbol == "." or symbol == "#":
                    item = Ground(x=x, y=y, width=self.platform_width, height=self.platform_height,
                                  image='blocks/platform.jpg')
                    entities.add(item)
                    platforms.append(item)
                if symbol == "f":
                    item = BonusBlock(x=x, y=y, width=self.platform_height, height=self.platform_height,
                                      images_existing=['blocks/bonus_block_active_1.png', 'blocks/bonus_block_active_2.png'],
                                      image_simple='blocks/bonus_block_simple.png', koef=20, activity=True,
                                      change_ability=True, type_bonus=1)
                    entities.add(item)
                    platforms.append(item)
                if symbol == "m":
                    item = BonusBlock(x=x, y=y, width=self.platform_height, height=self.platform_height,
                                      images_existing=['blocks/bonus_block_active_1.png', 'blocks/bonus_block_active_2.png'],
                                      image_simple='blocks/bonus_block_simple.png', koef=20, activity=True,
                                      change_ability=True, type_bonus=2)
                    entities.add(item)
                    platforms.append(item)
                if symbol == "s":
                    item = Slub(x=x, y=y, width=self.platform_height, height=self.platform_height,
                                images_existing=['enemies/simple_enemy/slub1.png', 'enemies/simple_enemy/slub2.png'],
                                image_killed='enemies/simple_enemy/slub3.png', koef=49, lifes=1, max_way=96, xvel=0,
                                yvel=0, gravity=1, move_speed=1,  left=True, right=False, up=False, on_ground=False,
                                changing=True)
                    monsters.add(item)
                    entities.add(item)
                    platforms.append(item)
                if symbol == "b":
                    item = Bowser(x=x, y=y, width=48, height=48, images_existing=[['enemies/bowser/bowser1_left.png',
                                  'enemies/bowser/bowser2_left.png'],['enemies/bowser/bowser1_right.png',
                                  'enemies/bowser/bowser2_right.png']], image_killed=['enemies/bowser/bowser1_left_die.png',
                                  'enemies/bowser/bowser1_right_die.png'],koef=9, side=True, lifes=5, max_way=96, xvel=0,
                                  yvel=0, gravity=1, move_speed=1, left=True, right=False, up=False, on_ground=False,
                                  changing=True)
                    monsters.add(item)
                    entities.add(item)
                    platforms.append(item)
                x += self.platform_height
            y += self.platform_height
            x = 0
