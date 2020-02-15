import diceroller


class AtmoDetailGenerator:
    def __init__(self, planet, seed, orbit, star, orbit_zone):
        self.planet = planet
        self.dice = diceroller(seed)
        self.orbit = orbit #  just the number
        self.orbit_zone = orbit_zone
        self.star = star
        self.composition = None
        self.pressure = None
        self.avg_temperature = None
        self.min_temperature = None
        self.max_temperature = None
        self.native_life = None
        self.terraforming = None

    def generate_composition(self):
        taints = ["Disease", "Gas Mix", "High Oxygen", "Pollutants", "Sulfur Compounds", "Pollutants",
                  "Sulfur Compounds", "Pollutants", "Low Oxygen", "Gas Mix", "Disease"]
        exotics = [("Very Thin", "Irritant"), ("Very Thin", "Non-Irritant"), ("Thin", "Non-Irritant"),
                   ("Thin", "Irritant"), ("Standard", "Non-Irritant"), ("Standard", "Irritant"),
                   ("Dense", "Non-Irritant"), ("Dense", "Irritant"), ("Very Dense", "Non-Irritant"),
                   ("Very Dense", "Irritant"), ("Occasional Corrosive", "Occasional Corrosive")]
        ctr = [(-273, -100), (-100, -25), (-25, 50), (50, 100), (-200, -25), (100, 600)] #  Corrosive Temperature Range
        corrosives = [("Trace", ctr[0]), ("Very Thin", ctr[1]), ("Very Thin", ctr[2]), ("Very Thin", ctr[3]),
                      ("Normal", ctr[4]), ("Normal", ctr[2]), ("Normal", ctr[3]), ("Very Dense", ctr[4]),
                      ("Very Dense", ctr[3]), ("Very Dense", ctr[5])]
        insidious = ["Gas Mix", "Gas Mix", "Radiation", "Temperature", "Pressure", "Gas Mix", "Pressure", "Temperature",
                     "Radiation", "Gas Mix", "Gas Mix"] # TODO replace GAS MIX with different mixes of gases
        comp_roll = self.dice.roll2d6() - 2
        if self.planet.uwp[2] == 2 or 4 or 7 or 9:
           self.composition = taints[comp_roll]
        elif self.planet.uwp[2] == 10:
            self.composition = exotics[comp_roll]
        elif self.planet.uwp[2] == 11:
            self.composition = corrosives[comp_roll]
        elif self.planet.uwp[2] == 12:
            self.composition = insidious[comp_roll]
        else:
            self.composition = "Standard Nitrogen/Oxygen Mix"
        return

    def convert_exceptional_atmospheres(self):
        if self.composition[0] == "Very Thin":
            uwp_equiv = 2
        elif self.composition[0] == "Thin":
            uwp_equiv = 4
        elif self.composition[0] == "Standard":
            uwp_equiv = 6
        elif self.composition[0] == "Dense":
            uwp_equiv = 8
        elif self.composition[0] == "Very Dense":
            uwp_equiv = 13
        else:
            print("Non Exceptional Atmosphere")
            uwp_equiv = None
        return uwp_equiv

    def generate_surface_pressure(self):
        trace = [0.01, 0.05, 0.05, 0.06 0.06, 0.07, 0.07, 0.07, 0.08, 0.08, 0.09]
        v_thin = [0.10, 0.12, 0.14, 0.16, 0.18, 0.20, 0.23, 0.25, 0.30, 0.35, 0.40]
        thin = [0.43, 0.45, 0.48, 0.50, 0.50, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75]
        stand = [0.76, 0.80, 0.85, 0.90, 0.95, 1.00, 1.00, 1.10, 1.20, 1.30, 1.40]
        dense = [1.50, 1.60, 1.70, 1.80, 1.90, 2.00, 2.00, 2.20, 2,20, 2.40, 2.40]
        v_dense = [2.50, 5.00, 10.00, 25.00, 50.00, 100.00, 150.00, 200.00, 250.00, 500.00, 750.00]
        if self.planet.uwp[2] == 10 or 11 or 12:
            wac = self.convert_exceptional_atmospheres() #  Working Atmosphere Code
        else:
            wac = self.planet.uwp[2]
        pressure_roll = self.dice.roll2d6() - 2
        if wac == 1:
            self.pressure = trace[pressure_roll]
        elif wac == 2 or 3:
            self.pressure = v_thin[pressure_roll]
        elif wac == 4 or 5:
            self.pressure = thin[pressure_roll]
        elif wac == 6 or 7:
            self.pressure = stand[pressure_roll]
        elif wac == 8 or 9:
            self.pressure = dense[pressure_roll]
        elif wac == 13 or 14:
            self.pressure = v_dense[pressure_roll]
        elif wac == 15:
            self.pressure = thin[pressure_roll] - 0.20
        else:
            print("Something has broken in the pressure generator")
        return

    def find_size_grou(self):
        if self.star.type ==
        return size_group

    def calc_luminosity(self):
        Ia_schedule = [27.36, 21.25, 18.09, 16.87, 15.75, 15.03, 16.09, 17.27, 17.65, 18.09, 18.49, 18.95, 19.38]
        Ib_schedule = [22.80, 14.70, 11.07, 10.40, 09.27, 08.45, 08.84, 09.49, 10.40, 11.95, 14.65, 17.27, 18.49]
        II_schedule = [20.31, 11.68, 06.85, 05.40, 04.95, 04.75, 04.86, 05.22, 05.46, 07.04, 08.24, 11.05, 11.28]
        III_schedule = [18.09, 09.05, 04.09, 03.08, 02.70, 02.56, 02.66, 02.94, 03.12, 04.23, 04.66, 06.91, 07.20]
        IV_schedule = [16.87, 06.69, 03.53, 02.47, 02.09, 01.86, 01.60, 01.49, 01.47, 99999, 99999, 99999, 99999]
        #  Final four values above are placeholder for non existent value, set ludicrously large for debugging
        V_schedule = [15.38, 06.12, 03.08, 02.00, 01.69, 01.37, 01.05, 00.90, 00.81, 00.53, 00.45, 00.29, 00.18]
        VI_schedule = [99999, 99999, 99999, 99999, 99999, 00.99, 00.75, 00.66, 00.58, 00.40, 00.32, 00.21, 00.09]
        #  First five values above are placeholder for non existent value, set ludicrously large for debugging
        D_schedule = {'B':0.46, 'A':0.27, 'F':0.13, 'G':0.09, 'K':0.08, 'M':0.07}

        if self.star.size == 'Ia':
            luminosity = Ia_schedule[self.star.orbit_table[1]]
            return luminosity
        elif self.star.size == 'Ib':
            luminosity = Ib_schedule[self.star.orbit_table[1]]
            return luminosity
        elif self.star.size == 'II':
            luminosity = II_schedule[self.star.orbit_table[1]]
            return luminosity
        elif self.star.size == 'III':
            luminosity = III_schedule[self.star.orbit_table[1]]
            return luminosity
        elif self.star.size == 'IV':
            luminosity = IV_schedule[self.star.orbit_table[1]]
            return luminosity
        elif self.star.size == 'V':
            luminosity = V_schedule[self.star.orbit_table[1]]
            return luminosity
        elif self.star.size == 'VI':
            luminosity = VI_schedule[self.star.orbit_table[1]]
            return luminosity
        elif self.star.size == "D"
            luminosity = D_schedule[self.star.type]
            return luminosity
        else:
            print("Luminosity Calc has gone wrong")
            return

    def calculate_asorbtion(self):
        hab_thin = [0.900, 0.829, 0.803, 0.811, 0.782, 0.789, 0.795, 0.802, 0.808, 0.814, 0.818]
        nohab_thin = [0.800, 0.744, 0.736, 0.752, 0.738, 0.753, 0.767, 0.782, 0.796, 0.810, 0.818]
        hab_stdense = [0.900, 0.900, 0.860, 0.860, 0.820, 0.780, 0.740, 0.700, 0.660, 0.620, 0.618]
        nohab_stdense = [0.800, 0.811, 0.789, 0.799, 0.774, 0.747, 0.718, 0.687, 0.654, 0.619, 0.619]
        hab_special = [0.740, 0.697, 0.672, 0.676, 0.648, 0.613, 0.577, 0.539, 0.500, 0.500, 0.500]
        nohab_special = [0.680, 0.646, 0.635, 0.644, 0.625, 0.599, 0.570, 0.537, 0.500, 0.500, 0.500]
        hab_E = [0.900, 0.900, 0.882, 0.883, 0.866, 0.850, 0.836, 0.821, 0.807, 0.793, 0.773]
        nohab_E = [0.800, 0.811, 0.807, 0.817, 0.813, 0.809, 0.805, 0.800, 0.794, 0.787, 0.773]
        if self.orbit_zone == "H":
            if self.planet.uwp[2] == 0 or 1 or 2 or 3:
                asorbtion =

    def calculate_surface_temperature(self):
        orbit_factor = [836.345, 591.385, 447.045, 274.025, 295.693, 223.523, 164.021, 118.277, 84.484, 60.046, 42.569,
                        30.140, 21.326, 15.085, 10.668, 7.544, 5.335, 3.772, 2.667, 1.886]

        gg_effect = [1.00, 1.00, 1.00, 1.00, 1.05, 1.05, 1.10, 1.10, 1.15, 1.15, self.gg_generate(), self.gg_generate(),
                     self.gg_generate(), 1.15, 1.10, 1.00]


    def gg_generate(self):
        a = [1.2, 1.2, 1.3, 1.3, 1.4, 1.4, 1.5, 1.5, 1.6, 1.6, 1.7]
        b = [1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2]
        gg_roll = self.dice.roll2d6()
        if self.pressure.uwp[2] == 10:
            return a[gg_roll]
        elif self.planet.uwp[2] == 10 or 11:
            return  b[gg_roll]
