from hashing import hash_code
class Gnome():
    def __init__(self, id=hash_code("gnome"), rainpower=5):
        # super().__init__(name, dice_type)
        self.id = id
        self.rainpower = rainpower
    def e(self):
        return print('✭')