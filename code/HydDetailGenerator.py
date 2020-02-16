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

    def generate_terraforming(self):
        terra_score = 0
        hydro_score = 0
        if self.planet.uwp[1] == 1 or 2:
            hydro_score += 2
            terra_score += 4
        elif self.planet.uwp[1] == 3 or 4:
            hydro_score += 1
            terra_score += 3
        elif self.planet.uwp[1] == 5 or 6:
            terra_score += 2
        elif self.planet.uwp[1] == 3 or 4:
            hydro_score += 1
            terra_score += 3
        elif self.planet.uwp[1] == 7 or 8:
            hydro_score -= 1
            terra_score += 1
        elif self.planet.uwp[1] >= 9:
            hydro_score -= 2
        if self.planet.uwp[2] == 0:
            hydro_score -= 4
            terra_score -= 4
        if self.planet.uwp[3] == 0:
            terra_score += 1
        elif 1 <= self.planet.uwp[3] <= 9:
            hydro_score += 1
        if self.planet.uwp[4] < 5:
            hydro_score -= 2
            terra_score -= 2
        elif self.planet.uwp[4] > 7:
            hydro_score += 2
            terra_score += 2
        if self.planet.uwp[7] < 5:
            hydro_score -= 10
            terra_score -= 10
        elif 5 <= self.planet.uwp[7] <= 8:
            hydro_score += 1
            terra_score += 1
        elif 9 <= self.planet.uwp[7] <= 11:
            hydro_score += 2
            terra_score += 3
        elif 12 <= self.planet.uwp[7]:
            hydro_score += 3
            terra_score += 4
        if not self.planet.atmo_details.native_life:
            hydro_score += 3
            terra_score += 3
        hydro_roll = self.dice.roll2d6()
        if hydro_score > hydro_roll:
            hydro_terra = True
        else:
            hydro_terra = False
        if terra_score > terra_roll:
            terra_terra = True
        else:
            terra_terra = False
        self.terraforming = [hydro_terra, terra_terra]
        if hydro_terra:
            modification = self.dice.roll1d3() + self.dice.roll1d3()
            if self.planet[3] < 5:
                self.percentage += modification
            else:
                self.percentage -= modification
        return
    def generate_continents(self):
        continent_lol = [[self.dice.roll2d6+1, self.dice.roll1d6()-1, self.dice.rollnd6(3)-3, self.dice.roll2d6()],
                        [self.dice.roll2d6+1, self.dice.roll2d6()-2, self.dice.rollnd6(3)-3, self.dice.roll2d6()],
                        [self.dice.roll2d6+1, self.dice.rollnd6(3)-3, self.dice.rollnd6(3)-3, self.dice.roll2d6()],
                        [self.dice.roll2d6, self.dice.roll1d6()-1, self.dice.rollnd6(3)-3, self.dice.roll2d6()],
                        [self.dice.roll2d6, self.dice.roll2d6()-2, self.dice.rollnd6(3)-3, self.dice.roll2d6()],
                        [self.dice.roll2d6, self.dice.rollnd6(3)-3, self.dice.rollnd6(3)-3, self.dice.roll2d6()],
                        [self.dice.roll1d6, self.dice.roll1d6() - 1, self.dice.rollnd6(3) - 3, self.dice.roll2d6()],
                        [self.dice.roll1d6, self.dice.roll2d6() - 2, self.dice.rollnd6(3) - 3, self.dice.roll2d6()],
                        [self.dice.roll1d6, self.dice.rollnd6(3) - 3, self.dice.rollnd6(3) - 3, self.dice.roll2d6()],
                        [self.dice.roll1d6 - 1 , self.dice.roll1d6(), self.dice.rollnd6(3) - 3, self.dice.roll2d6()],
                        [self.dice.roll1d6 - 1, self.dice.roll2d6(), self.dice.rollnd6(3) - 3, self.dice.roll2d6()],
                        [self.dice.roll1d6 - 1 , self.dice.rollnd6(3), self.dice.rollnd6(3) - 3, self.dice.roll2d6()],
                        [self.dice.roll1d6 - 2, self.dice.roll1d6() - 1, self.dice.rollnd6(3) - 3, self.dice.roll2d6()],
                        [self.dice.roll1d6 - 3, self.dice.roll1d6() - 2, self.dice.rollnd6(3) - 3, self.dice.roll2d6()],
                        [self.dice.roll1d6 - 4, self.dice.roll1d6() - 3, self.dice.roll2d6(), self.dice.roll2d6()],
                        [0, 0, self.dice.roll1d6() - 3, self.dice.roll2d6()],
                        [0, 0, 0, self.dice.roll2d6()],
                        [0, 0, 0, self.dice.roll2d6()],
                        [0, 0, 0, self.dice.roll1d6()],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]]
        if self.percentage >= 50:
            land_roll = self.dice.roll1d6()
            land_index = land_roll + self.planet.uwp[3] * 3
            self.continents = continent_lol[land_index - 16]
            # TODO fix negative values
            return
        else:
            if self.percentage == 0:
                self.continents = [1,0,0,0]
            else:
                self.continents = [1, 2, 3, 4]
            return
    def generat_oceans(self):
        oceans_lol = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, self.dice.roll1d6()],
                      [0, 0, 0, self.dice.roll2d6()],
                      [0, 0, 0, self.dice.roll2d6()],
                      [0, 0, self.dice.roll1d6() - 3, self.dice.roll2d6()],
                      [self.dice.roll1d6() - 4, self.dice.roll1d6() - 3, self.dice.roll2d6() - 3 , self.dice.roll2d6],
                      [self.dice.roll1d6() - 4, self.dice.roll1d6() - 2, self.dice.rollnd6(3) - 3 , self.dice.roll2d6],
                      [self.dice.roll1d6() - 3, self.dice.roll1d6() - 1, self.dice.rollnd6(3) - 3, self.dice.roll2d6],
                      [self.dice.roll1d6() - 3, self.dice.roll1d6() - 1, self.dice.rollnd6(3) - 3, self.dice.roll2d6],
                      [self.dice.roll1d6() - 2, self.dice.roll1d6() - 1, self.dice.rollnd6(3) - 3, self.dice.roll2d6],
                      [self.dice.roll1d6() - 2, self.dice.roll2d6() - 2, self.dice.rollnd6(3) - 3, self.dice.roll2d6],
                      [self.dice.roll1d6() - 1, self.dice.roll1d6() - 1, self.dice.rollnd6(3) - 3, self.dice.roll2d6],
                      [self.dice.roll1d6() - 1, self.dice.roll2d6() - 2, self.dice.rollnd6(3) - 3, self.dice.roll2d6],
                      [self.dice.roll1d6() - 1, self.dice.rollnd6(3) - 3, self.dice.rollnd6(3) - 3, self.dice.roll2d6],
                      [self.dice.roll1d6(), self.dice.roll1d6() - 1, self.dice.rollnd6(3) - 3, self.dice.roll2d6],
                      [self.dice.roll1d6(), self.dice.roll2d6() - 2, self.dice.rollnd6(3) - 3, self.dice.roll2d6],
                      [self.dice.roll1d6(), self.dice.rollnd6(3) - 3, self.dice.rollnd6(3) - 3, self.dice.roll2d6],
                      [1, self.dice.roll1d6() - 1, self.dice.rollnd6(3) - 3, self.dice.roll2d6],
                      [1, self.dice.roll2d6() - 2, self.dice.rollnd6(3) - 3, self.dice.roll2d6],
                      [1, self.dice.rollnd6(3) - 3, self.dice.rollnd6(3) - 3, self.dice.roll2d6]]
        if self.percentage < 50:
            ocean_roll = self.dice.roll1d6()
            ocean_index = ocean_roll + self.planet.uwp[3] * 3
            self.oceans =oceans_lol[ocean_index - 1]
            # TODO fix negative values
            return
        else:
            if self.percentage == 100:
                self.oceans = [1,0,0,0]
            else:
                self.oceans = [0, 1, 3, 4]
            return

