import diceroller


class Star:
    """
           A class used to roll dice for use in the digital

           ...

           Attributes
           ----------
           name : str
                The name of the star

           type : str
               Stellar Type from Sequence OBAFGKM combined with a decimal classification

           size : str
               Stellar Size

            dice : DiceRoller
               A set of dice that allows consistent dice rolls. This relies on a set seed which is defined in the class
               definition.

            orbit_table : list
                Reference for orbit table in Orbits -> OrbitTable -> master_table


            is_companion : bool
                Is the Star a companion

           Methods
           -------
           create_star(dice_mod = 0)
                Generates the Type and Size of the star and calls on further creation methods.
                Dice Mod exists to allow for retrogeneration of systems from existing UWPs.

            generate_decimal()
                Appends the decimal classification to the Star Type

            verify_star_size()
                Confirms that star type is a valid for star size, if not corrects star size

           """

    def __init__(self, seed):
        self.name = seed
        self.type = None
        self.size = None
        self.dice = diceroller(seed)
        self.orbit_table = None
        self.is_companion = False

    def create_star(self, dice_mod=0):
        type_roll = self.dice.roll_2d6() + dice_mod
        size_roll = self.dice.roll_2d6() + dice_mod
        if type_roll == 2:
            self.type = 'A'
        elif type_roll == 8:
            self.type = 'K'
        elif type_roll == 9:
            self.type = 'G'
        elif 10 <= type_roll:
            self.type = 'F'
        elif 3 <= type_roll <= 7:
            self.type = 'M'
        else:
            print("INVALID TYPE ROLL")
        if size_roll == 2:
            self.size = 'II'
        elif size_roll == 3:
            self.size = 'III'
        elif size_roll == 4:
            self.size = 'IV'
        elif 5 <= size_roll <= 10:
            self.size = 'V'
        elif size_roll == 11:
            self.size = 'VI'
        elif size_roll == 12:
            self.size = 'D'
        else:
            print("INVALID SIZE ROLL")
        self.generate_decimal()
        self.verify_star_size()
        self.determine_orbit_table()
        return

    def generate_decimal(self):
        decimal = self.dice.roll2d6() - 2
        self.type = self.type + str(decimal)
        return

    def verify_star_size(self):
        if self.type[0] == 'K' and self.type[1] > 4 and self.size == "IV":
            self.size = "V"
        elif self.type[0] == 'M' and self.size == "IV":
            self.size = "V"
        elif self.type[0] == 'A' or 'F' or 'G' and self.size == "II" or "III":
            self.size = "V"
        else:
            print("Invalid Star Type")
        return

    def determine_orbit_table(self):
        self.orbit_table = []
        if self.size == "Ia":
            self.orbit_table[0] = 0
        elif self.size == "Ib":
            self.orbit_table[0] = 1
        elif self.size == "II":
            self.orbit_table[0] = 2
        elif self.size == "III":
            self.orbit_table[0] = 3
        elif self.size == "IV":
            self.orbit_table[0] = 4
        elif self.size == "V":
            self.orbit_table[0] = 5
        elif self.size == "VI":
            self.orbit_table[0] = 6
        elif self.size == "D":
            self.orbit_table[0] = 7
        else:
            print("Invalid Star Size")
        if self.type == "B0" or "B1" or "B2" or "B3" or "B4":
            self.orbit_table[1] = 0
        elif self.type == "B5" or "B6" or "B7" or "B8" or "B9":
            self.orbit_table[1] = 1
        elif self.type == "A0" or "A1" or "A2" or "A3" or "A4":
            self.orbit_table[1] = 2
        elif self.type == "A5" or "A6" or "A7" or "A8" or "A9":
            self.orbit_table[1] = 3
        elif self.type == "F0" or "F1" or "F2" or "F3" or "F4":
            self.orbit_table[1] = 4
        elif self.type == "F5" or "F6" or "F7" or "F8" or "F9":
            self.orbit_table[1] = 5
        elif self.type == "G0" or "G1" or "G2" or "G3" or "G4":
            self.orbit_table[1] = 6
        elif self.type == "G5" or "G6" or "G7" or "G8" or "G9":
            self.orbit_table[1] = 7
        elif self.type == "K0" or "K1" or "K2" or "K3" or "K4":
            self.orbit_table[1] = 8
        elif self.type == "K5" or "K6" or "K7" or "K8" or "K9":
            self.orbit_table[1] = 9
        elif self.type == "M0" or "M1" or "M2" or "M3" or "M4":
            self.orbit_table[1] = 10
        elif self.type == "M5" or "M6" or "M7" or "M8":
            self.orbit_table[1] = 11
        elif self.type == "M9":
            self.orbit_table[1] = 12
        else:
            print("Invalid Star Type")
        return

