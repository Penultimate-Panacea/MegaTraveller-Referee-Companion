import diceroller

stellar_orbit_tables = {}

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

            orbit_table : str
                Returns index of orbit table


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

    def create_star(self, dice_mod = 0):
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
        return

    def generate_decimal(self):
        a = self.dice.roll1d6()
        if a % 2 == 0:
            b = 5
            while b == 5:
                b = self.dice.roll1d6() - 1
            self.type = self.type + str(b)
            return
        elif a % 2 == 1:
            b = 10
            while b == 10:
                b = self.dice.roll1d6 + 4
            self.type = self.type + str(b)
            return
        else:
            print ("INVALID DECIMAL GEN")
            return

    def verify_star_size(self):
        if self.type[0] == 'K' and self.type[1] < 4 and self.size == "IV":
            self.size = "V"
        elif self.type[0] == 'M' and self.size == "IV":
            self.size = "V"
        return

    def determine_orbit_table(self):
        self.orbit_table = ""
        if self.size == "Ia":
            self.orbit_table += str(0)
        elif self.size == "Ib":
            self.orbit_table = str(1)
        elif self.size == "II":
            self.orbit_table = str(2)
        elif self.size == "III":
            self.orbit_table = str(3)
        elif self.size == "IV":
            self.orbit_table = str(4)
        elif self.size == "V":
            self.orbit_table = str(5)
        elif self.size == "VI":
            self.orbit_table = str(6)
        elif self.size == "D":
            self.orbit_table = str(7)
        else:
            print("Invalid Star Size")
            return

