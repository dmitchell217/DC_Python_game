from hashing import hash_code
class Plant():
    def __init__(self, id=hash_code("plant"), age=0, water=5, absorb = 5, wither=5, fruit = 0):
        self.id = id
        self.age = age
        self.water = water
        self.absorb = absorb
        self.wither = wither
        self.fruit = fruit
        # self.emoji = '✿'
    def run_day(self):
        self.age +=1
        # watering plants is automatic for now, once per day. Eventually will be input driven
        # self.water()
    # self.wilt()
    # self.sprout()

    # def colorize()
# newPlant = Plant()
# print(newPlant.emoji)