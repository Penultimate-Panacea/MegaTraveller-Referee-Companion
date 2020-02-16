import diceroller


class Resources:
    def __init__(self, planet, seed, orbit, star, orbit_zone):
        self.planet = planet
        self.dice = diceroller(seed)
        self.natural = None
        self.processed = None
        self.manufactured = None
        self.information = None
    def generate_natural(self):
        significant_natural = [False, False, False]
        agroproducts_score = 0
        metals_score = 0
        nonmetals_score = 0
        if self.planet.size_details.core == "Heavy Core":
            metals_score += 2
            nonmetals_score += 1
        elif self.planet.size_details.core == "Molten Core":
            agroproducts_score += 1
        elif self.planet.size_details.core == "Rocky Body":
            agroproducts_score += 1
        elif self.planet.size_details.core == "Icy Body":
            metals_score -= 1
            nonmetals_score -= 1
        else:
            print("INVALID CORE TYPE")
        if 4 <= self.planet.uwp[2] <= 9:
            agroproducts_score += 2
            nonmetals_score += 1
        elif self.planet.uwp[2] == 0 or 1 or 2 or 3 or 10:
            metals_score += 1
            nonmetals_score += 1
        if 0 <= self.planet.uwp[4] <= 4:
            agroproducts_score += 1
            metals_score -= 1
        elif self.planet.uwp[4] > 4:
            agroproducts_score += 2
            metals_score += 1
            nonmetals_score += 1
        if self.planet.uwp[7] < 4:
            agroproducts_score += 1
            metals_score -= 1
        elif self.planet.uwp[7] == 4 or 5 or 6:
            agroproducts_score += 2
            metals_score += 2
            nonmetals_score += 2
        elif 7 <= self.planet.uwp[7] <= 11:
            agroproducts_score += 1
            metals_score += 4
            nonmetals_score += 4
        elif self.planet.uwp[7] > 11:
            agroproducts_score += 1
            metals_score += 5
            nonmetals_score += 6
        if self.planet.atmo_details.native_life:
            agroproducts_score += 5
            nonmetals_score += 3
        agroproducts_roll = self.dice.roll2d6()
        metals_roll = self.dice.roll2d6()
        nonmetals_score = self.dice.roll2d6()
        if agroproducts_score > agroproducts_roll:
            significant_natural[0] = True
        if metals_score > metals_roll:
            significant_natural[1] = True
        if nonmetals_score > nonmetals_score:
            significant_natural[2] = True
        return

