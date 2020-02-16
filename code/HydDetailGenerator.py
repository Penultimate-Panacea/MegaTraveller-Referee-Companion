import diceroller

class HydDetailGenerator:
    def __init__(self, planet, seed, orbit, star, orbit_zone):
        self.planet = planet
        self.dice = diceroller(seed)
        self.orbit = orbit  # just the number
        self.orbit_zone = orbit_zone
        self.star = star
        self.percentage = None
        self.composition = None
        self.tectonic_plates = None
        self.terraforming = None
        self.continents = None
        self.oceans = None
        self.volcanoes = None
        self.weather_control = None

    def generate_percentage(self):
        percent_roll = self.dice.roll2d6() - 7
        percent = self.planet.uwp[3] * 10 + percent_roll
        self.percentage = percent
        return

