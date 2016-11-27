
class Heroes:

    def __init__(self, lst=[]):
        self.__lst = lst

    @property
    def lst(self):
        return self.__lst

    @lst.setter
    def lst(self, value = []):
        self.__lst = value

    def not_exist(self):
        if isinstance(self, Heroes):
            for i in self.lst:
                if i.lifes != 0:
                    return False
            return True

    def set_last_hero(self):
        if isinstance(self, Heroes):
            if len(self.lst) == 0:
                return False
            if len(self.lst) == 1:
                return self.lst[0]
            return self.lst[0] if self.lst[0].rect.x < self.lst[1].rect.x else self.lst[1]

    def append(self, *other):
        for item in other:
            self.__lst.append(item)

    def killed(self, hero, entities):
        hero.lifes = -1
        if hero.lifes == 0:
            entities.remove(hero)
            self.lst.remove(hero)
            del hero
        else:
            hero.move_to_start()

    def get_lives(self):
        array=[]
        for hero in self.lst:
            if hero.fire_ability and hero.flower_ability:
                array.append('{0} - {1}  Jump - {2}  Fire - {3}'.format(hero.type, hero.lifes, hero.time_flower_activity // 10000, hero.time_mushroom_activity//10000))
            elif hero.fire_ability and not hero.flower_ability:
                array.append('{0} - {1}  Fire - {2}'.format(hero.type, hero.lifes, hero.time_mushroom_activity //10000))
            elif hero.flower_ability and not hero.fire_ability:
                array.append('{0} - {1}  Jump - {2}'.format(hero.type, hero.lifes, hero.time_flower_activity // 10000))
            else:
                array.append('{0} - {1}'.format(hero.type, hero.lifes))
                                           # u'\u2764'* hero.lifes
        return array

    def set_default_settings(self):
        for hero in self.lst:
            hero.power = 1
            hero.super_hero = False
            hero.time_flower_activity = 0
            hero.time_mushroom_activity = 0
            hero.get_simple_jump()
            hero.fire_ability = False
            hero.flower_ability = False
            hero.move_to_start()

    def update_keys(self, settings):
        for i in range(len(self.lst)):
            self.lst[i].key_up=settings[0+i*4]
            self.lst[i].key_left=settings[i*4+1]
            self.lst[i].key_right=settings[i*4+2]
            self.lst[i].key_fire=settings[i*4+3]
