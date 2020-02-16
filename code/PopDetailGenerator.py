import diceroller


class PopDetailGenerator:
    def __init__(self, planet, seed):
        self.planet = planet
        self.dice = diceroller(seed)
        self.total_population = None
        self.unallocated_population = None
        self.very_large_cities = None
        self.large_cities = None
        self.medium_large_cities = None
        self.moderate_cities = None
        self.small_cities = None
        self.very_small_cities = None
        self.orbital_cities = None

    def calc_total_population(self):
        total_pop = self.planet.pop_multiplier * 10 ^ self.planet.uwp[4]
        self.total_population = total_pop
        return

