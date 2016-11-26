from model.entity.dead.Bonus import Bonus


class Mushroom(Bonus):
    def __init__(self, x=0, y=0, width=0, height=0, start_image='', images_appearing=[],images_existing=[], koef=0,
                 time_activity=0, change_ability=False):

        super().__init__(x, y, width, height,start_image, images_appearing,images_existing, koef,
                 time_activity, change_ability)
