import diceroller


class AtmoDetailGenerator:
    def __init__(self, planet, seed, orbit):
        self.planet = planet
        self.dice = diceroller(seed)
        self.orbit = orbit
        self.composition = None
        self.pressure = None
        self.avg_temperature = None
        self.min_temperature = None
        self.max_temperature = None
        self.native_life = None
        self.terraforming = None

    

