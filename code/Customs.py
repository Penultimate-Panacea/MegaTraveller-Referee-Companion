import diceroller


class Customs:
    def __init__(self, planet, seed):
        self.planet = planet
        self.dice = diceroller(seed)
        self.customs = None

