import random


class Warrior:

    def __init__(self):
        self.degat = random.choice(range(3, 5))
        self.chance = 5
        self.fuite = 3
        self.prix = 10
        self.type = "Warrior"
