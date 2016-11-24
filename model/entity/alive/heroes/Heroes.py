
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
            if hero.type == "hero2":
                self.lst.pop(0)
        else:
            hero.move_to_start()




