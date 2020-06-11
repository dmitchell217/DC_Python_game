import random
from hashing import hash_code
typeconvert = {"tree":Tree, "woodchuck":Woodchuck, "gnome":Gnome}
class Garden():
    # think about adding fruit and money to the garden object so I can keep track more easily
    def __init__(self, trees={}, gnomes={}, woodchucks={}, fruit=0, money=0):
        # self.trees = trees
        # self.gnomes = gnomes
        # self.woodchucks = woodchucks
        self.in_garden = {"trees":trees, "gnomes":gnomes, "woodchucks":woodchucks}
        self.fruit = fruit
        self.money = money
    def info(self):
        return (f" Your garden has the following items in it: \n {len(self.trees)} trees, \n {len(self.gnomes)} gnomes, \n and {len(self.woodchucks)} woodchucks \n  You have {self.fruit} fruit and ${self.money} under your mattress")
    

    def add_item(self, itemtype, num=1):
        self.in_garden[itemtype+"s"][random.randint(1,1000000)]=typeconvert[itemtype]()




    # def add_tree(self, num=1):
    #     self.trees.append([Tree])
    # def add_gnome(self, num=1):
    #     pass
    # def add_woodchuck(self, num=1):
    #     pass
    # def remove_tree(self, num=1):
    #     pass
    # def remove_gnome(self, num=1):
    #     pass
    # def remove_woodchuck(self, num=1):
    #     pass


class Plant():
    def __init__(self, id, age, water, absorb, wither, fruit = 0):
        self.id = id
        self.age = age
        self.water = water
        self.absorb = absorb
        self.wither = wither
        self.fruit = fruit
    def run_day(self):
        self.age +=1
        # watering plants is automatic for now, once per day. Eventually will be input driven
        self.water()
    # self.wilt()
    # self.sprout()

    # def colorize()

class Tree(Plant):
    def __init__(self, id, age, water = 10, absorb = 5, wither = 10, fruit=0, shade = 2):
        super().__init__(id, age) 
        # self.shade = shade
        self.wither = wither - shade
        self.WATERCAP = 30

    def wilt(self):
        self.water -= self.wither
    def sprout(self):
        if self.water >= self.WATERCAP:
            self.fruit+=1
            self.water = 10
    def grow(self):
        self.water += self.absorb
        return self.water
    def run_day(self):
        super().run_day() 
        self.wilt()
        self.sprout()
        

    
    





