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

    def generate_compositon(self):
        if self.planet.uwp[2] == 3 or 5 or 6 or 8:
            self.composition = "Water"
            return
        elif self.planet.uwp[2] == 2 or 4 or 7 or 9:
            self.composition = "Tainted Water"
            return
        elif self.planet.uwp[2] == 10:
            if self.dice.roll2d6() > 9:
                self.composition = "Tainted Liquid Water"
                return
            else:
                self.composition = "Atmosphere Related Chemical Mix"
                return
        elif self.planet.uwp[2] == 11 or 12:
            self.composition = "Atmosphere Related Chemical Mix"
            return
        else:
            self.composition = "Special Case (needs further study)"
            return
    def generate_tectonic(self):
        base = self.planet.uwp[1] + self.planet.uwp[2]
        roll = self.dice.roll2d6()
        self.tectonic_plates = base - roll
        return

