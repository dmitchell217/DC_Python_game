import random
class Garden():
    def __init__(self, trees, gnomes, woodchucks, rain = 5):
        pass

class Tree(Garden):
    def __init__(self, id, shade = 2, water = 100):
        # super().__init__(name, dice_type)
        self.id = id
        self.shade = shade
        self.water = water
    pass

class Gnome(Garden):
    def __init__(self, id, rainpower=5):
        # super().__init__(name, dice_type)
        self.id = id
        self.rainpower = rainpower
