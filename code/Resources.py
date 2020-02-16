import diceroller


class Resources:
    def __init__(self, planet, seed, orbit, star, orbit_zone):
        self.planet = planet
        self.dice = diceroller(seed)
        self.natural = None
        self.processed = None
        self.manufactured = None
        self.information = None


