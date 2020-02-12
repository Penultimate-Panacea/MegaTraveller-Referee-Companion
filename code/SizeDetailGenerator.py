import DiceRoller


class PlanetSize:
    def __init__(self, seed):
        self.dice = DiceRoller(seed)
        self.diameter = None
        self.density = None
        self.core = None
        self.mass = None
        self.gravity = None
