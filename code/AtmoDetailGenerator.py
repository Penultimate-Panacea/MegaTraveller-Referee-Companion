import diceroller


class AtmoDetailGenerator:
    def __init__(self, planet, seed, orbit, star):
        self.planet = planet
        self.dice = diceroller(seed)
        self.orbit = orbit #  just the number
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

    def generate_surface_pressure(self):
        Ia_schedule = [27.36, 21.25, 18.09, 16.87, 15.75, 15.03, 16.09, 17.27, 17.65, 18.09, 18.49, 18.95, 19.38]
        Ib_schedule = [22.80, 14.70, 11.07, 10.40, 09.27, 08.45, 08.84, 09.49, 10.40, 11.95, 14.65, 17.27, 18.49]
        II_schedule = [20.31, 11.68, 06.85, 05.40, 04.95, 04.75, 04.86, 05.22, 05.46, 07.04, 08.24, 11.05, 11.28]
        III_schedule = [18.09, 09.05, 04.09, 03.08, 02.70, 02.56, 02.66, 02.94, 03.12, 04.23, 04.66, 06.91, 07.20]
        IV_schedule = [16.87, 06.69, 03.53, 02.47, 02.09, 01.86, 01.60, 01.49, 01.47, 99999, 99999, 99999, 99999]
        #  Final four values above are placeholder for non existent value, set ludicrously large for debugging
        V_schedule = [15.38, 06.12, 03.08, 02.00, 01.69, 01.37, 01.05, 00.90, 00.81, 00.53, 00.45, 00.29, 00.18]
        VI_schedule = [15.38, 06.12, 03.08, 02.00, 01.69, 01.37, 01.05, 00.90, 00.81, 00.53, 00.45, 00.29, 00.18]
        #  First five values above are placeholder for non existent value, set ludicrously large for debugging