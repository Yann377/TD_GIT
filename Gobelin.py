import random


class Gobelin:
    def __init__(self):
        self.degat = random.choice(range(2, 3))
        self.loot = random.choice([1, 1.5])

