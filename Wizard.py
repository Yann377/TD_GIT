import random

class Wizard:

    def __init__(self):
        self.degat = random.choice(2,4)
        self.chance = 20
        self.fuite = 10
        self.prix = 15
        self.type = "Wizard"