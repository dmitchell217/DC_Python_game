from plant import Plant
from hashing import hash_code
class Tree(Plant):
    def __init__(self, age=0, water = 10, absorb = 15, wither = 10, fruit=0, shade = 2):
        super().__init__() 
        # self.shade = shade
        self.wither = wither - shade
        self.WATERCAP = 30
        # add in death feature
        self.DEADCAP = -10
        self.id = hash_code("tree")
        self.emoji_fruit = '＄'
        self.emoji_sprout = '✿'
        self.emoji_dead = ''
        self.absorb = absorb

    def wilt(self):
        self.water -= self.wither
    def harvest(self):
        if self.water >= self.WATERCAP:
            self.water = 10
            return True
        return False
    def grow(self):
        self.water += self.absorb
        return self.water
    def run_day(self):
        super().run_day() 
        self.wilt()
    def e(self):
        if self.water > self.WATERCAP:
            return self.emoji_fruit
        else:
            return self.emoji_sprout


# newGnome = Tree()
# print(newGnome.id)
# newGnome = Tree()
# print(newGnome.id)
# newGnome2 = Tree()
# print(newGnome2.id)