import diceroller


class Resources:
    def __init__(self, planet, seed, orbit, star, orbit_zone):
        self.planet = planet
        self.dice = diceroller(seed)
        self.natural = None
        self.processed = None
        self.manufactured = None
        self.information = None
    def generate_processed(self):
        significant_processed = [False, False, False]
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
        nonmetals_roll = self.dice.roll2d6()
        if agroproducts_score > agroproducts_roll:
            significant_processed[0] = True
        if metals_score > metals_roll:
            significant_processed[1] = True
        if nonmetals_score > nonmetals_roll:
            significant_processed[2] = True
        return

    def generate_natural(self):
        significant_natural = [False, False, False, False, False]
        agricultural_score = 0
        ores_score = 0
        radioactives_score = 0
        crystals_score = 0
        compounds_score = 0
        agricultural_roll = self.dice.roll2d6()
        ores_roll = self.dice.roll2d6()
        radioactives_roll = self.dice.roll2d6()
        crystals_roll = self.dice.roll2d6()
        compounds_roll = self.dice.roll2d6()
        if self.planet.size_details.core == "Heavy Core":
            agricultural_score += 1
            ores_score += 8
            radioactives_score += 7
            crystals_score += 6
            compounds_score += 5
        elif self.planet.size_details.core == "Molten Core":
            agricultural_score += 4
            ores_score += 7
            radioactives_score += 5
            crystals_score += 5
            compounds_score += 6
        elif self.planet.size_details.core == "Rocky Body":
            agricultural_score += 4
            ores_score += 3
            radioactives_score += 3
            crystals_score += 2
            compounds_score += 1
        elif self.planet.size_details.core == "Icy Body":
            agricultural_score -= 4
            compounds_score -= 4
        else:
            print("INVALID CORE TYPE")
        if 4 <= self.planet.uwp[2] <= 9:
            agricultural_score += 1
        elif 0 <= self.planet.uwp[2] <= 3 or 10 <= self.planet.uwp[2]:
            agricultural_score -= 3
            ores_score += 1
            radioactives_score += 1
            compounds_score += 1
        if 0 <= self.planet.uwp[7] <= 3
            agricultural_score += 1
            ores_score += 1
            radioactives_score += 1
            crystals_score += 1
            compounds_score += 1
        elif 7 <= self.planet.uwp[7] <= 11:
            agricultural_score -= 1
        elif 12 <= self.planet.uwp[7]:
            agricultural_score -= 2
            ores_score += 1
            radioactives_score += 1
            crystals_score += 1
            compounds_score += 1
        if self.planet.atmo_details.native_life:
            agricultural_score += 5
            compounds_score += 1
        elif not self.planet.atmo_details.native_life:
            compounds_score -= 1
        else:
            print("Failure in Atmo Life Gen")
        if agricultural_score > agricultural_roll:
            significant_natural[0] = True
        if ores_score > ores_roll:
            significant_natural[1] = True
        if radioactives_score > radioactives_roll:
            significant_natural[2] = True
        if crystals_score > crystals_roll:
            significant_natural[3] = True
        if compounds_score > compounds_roll:
            significant_natural[4] = True
        return



