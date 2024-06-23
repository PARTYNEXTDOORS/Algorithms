import random

class RandomizedSet:

    def __init__(self):
        self.elem = set()
        

    def insert(self, val: int) -> bool:
        if val in self.elem:
            return False
        else:
            self.elem.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.elem:
            self.elem.discard(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        if len(self.elem) != 0:
            return random.choice(list(self.elem))
