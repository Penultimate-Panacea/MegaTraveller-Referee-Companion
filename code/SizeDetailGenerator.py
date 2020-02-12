import DiceRoller

class PlanetSize():
    def __init__(self, seed, uwp=None):
        if uwp is None:
            self.uwp = ['X', 0, 0, 0, 0, 0, 0, 0] #TODO UWP Class
        self.dice = DiceRoller(seed)
        self.diameter = None
        self.density = None
        self.core = None
        self.mass = None
        self.gravity = None
        self.is_outer_orbit = False #TODO Inherit Orbit data or create setter function

    def generate_diameter(self):
        flux = self.dice.roll2d6() - 7
        flux *= 100
        self.diameter = self.uwp[1] * 1000
        self.diameter += flux
        self.diameter += self.dice.rolld00()
        return

    def generate_core(self):
        dice_mods = 0
        if self.uwp[1] <= 4:
            dice_mods += 1
        if self.uwp[1] >= 6:
            dice_mods -= 2
        if self.uwp[2] <= 3:
            dice_mods += 1
        if self.uwp[2] >= 6:
            dice_mods -=2
        if self.is_outer_orbit:
            dice_mods += 6
        density_roll = self.dice.roll2d6() + dice_mods
        if density_roll >= 1:
            self.core = "Heavy Core"
            return
        if 2 >= density_roll >= 10:
            self.core = "Molten Core"
            return
        if 11 >= density_roll >= 14:
            self.core = "Rocky Body"
            return
        if density_roll >= 14:
            self.core = "Icy Body"
            return

    def generate_density(self):
        heavy_core = [1.10, 1.15, 1.20, 1.25, 1.30, 1.35, 1.40, 1.45, 1.50, 1.55, 1.60, 1.70, 1.80, 1.90, 2.00, 2.25]
        molten_core = [0.82, 0.84, 0.86, 0.88, 0.90, 0.92, 0.94, 0.96, 0.98, 1.00, 1.02, 1.04, 1.06, 1.08, 1.10, 1.12]
        rocky_body = [0.50, 0.52, 0.54, 0.56, 0.58, 0.60, 0.62, 0.64, 0.66, 0.68, 0.70, 0.72, 0.74, 0.76, 0.78, 0.80]
        icy_body = [0.18, 0.20, 0.22, 0.24, 0.26, 0.28, 0.30, 0.32, 0.34, 0.36, 0.38, 0.40, 0.42, 0.44, 0.46, 0.48]
        density_roll = self.dice.rollnd6(3)
        if self.core == "Heavy Core":
            self.density = heavy_core[density_roll - 3]
            return
        if self.core == "Molten Core":
            self.density = molten_core[density_roll - 3]
            return
        if self.core == "Rocky Body":
            self.density = rocky_body[density_roll - 3]
            return
        if self.core == "Icy Body":
            self.density = icy_body[density_roll - 3]
            return

    def generate_mass(self):
        uwp_calc = self.uwp[1] / 8
        uwp_calc ^= 3
        self.mass = self.density * uwp_calc
        return

    def generate_gravity(self):
        uwp_calc = (self.uwp[1]) ^ 2
        uwp_calc = 64 / uwp_calc
        self.gravity = self.mass * uwp_calc

    def generate_size_data(self):
        self.generate_diameter()
        self.generate_core()
        self.generate_density()
        self.generate_mass()
        self.generate_gravity()

