from hashing import hash_code
class Gnome():
    def __init__(self, id='', rainpower=5):
        # super().__init__(name, dice_type)
        self.id = hash_code("gnome")
        self.rainpower = rainpower
    def e(self):
        return print('✭')
# newGnome = Gnome()
# print(newGnome.id)
# newGnome = Gnome()
# print(newGnome.id)
# newGnome2 = Gnome()
# print(newGnome2.id)