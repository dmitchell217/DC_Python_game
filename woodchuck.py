from hashing import hash_code
class Woodchuck():
    def __init__(self, id=hash_code("woodchuck"), peck = 5):
        self.peck = peck
        self.id = id
    def e(self):
        return print('✖')