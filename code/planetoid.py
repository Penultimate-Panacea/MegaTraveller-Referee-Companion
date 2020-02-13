from diceroller import diceroller


class Planetoid:
    def __init__(self):
        self.size_details = None
        self.atmo_details = None
        self.hydr_details = None
        self.pops_details = None
        self.govt_details = None
        self.lawl_details = None
        self.name = None


class PlanetoidBelt:
    """
    A class used to store data about Planetoid Belts

    ...

    Attributes
    ----------
    dice : DiceRoller
        A set of dice that allows consistent dice rolls. This relies on a set seed which is defined in the class
        definition.

    orbit : int
        Which orbit the belt is in

    star : Star
        #TODO

    dom_diameter : str
        Diameter of the dominant planetoids (30% of belt falls into this category) This is a string because it is not
        used in any calculations

    dom_tons : str
        Displacement Tons of dominant planetoids

    max_diameter : str
        Diameter of the largest planetoids (less than 1% of belt falls into this category)

    max_tons : str
        Displacement tons of largest planetoids

    zone : char
        The primary the belt falls into. N represents Ferrous-Nickle bodies, M represents Mixed bodies, C represents icy
        bodies

    composition : list
        Percent composition of n, m, and c bodies in a belt. If the percentages are greater than 100, they overlap

    width : float
        Width of the belt, measured in AU


    Methods
    -------
    generate_diameters()
        Generates the diameters of bodies in a belt

    generate_zone()
        Generates the zone of the belt

    generate_composition()
        Generates the composition of the belt

    generate_width()
        Generates the width of the belt

    generate_belt()
        Calls all previous generate methods to generate a belt in one fell swoop

    output_belt()
        returns a string which describes the belt in the format as described in the WBH

    """

    def __init__(self, seed):
        self.dice = diceroller(seed)
        self.orbit = None
        self.star = None
        self.dom_diameter = None
        self.dom_tons = None
        self.max_diameter = None
        self.max_tons = None
        self.zone = None
        self.composition = None
        self.width = None

    def generate_diameters(self):
        diameters = ["1m", "5m", "10m", "25m", "50m", "100m", "300m", "1km", "5km", "50km", "500km"]
        tons = [">1t", "5t", "50t", "500t", "5kt", "50kt", "1Mt", "50Mt", "5Gt", "5Tt", "5Pt"]
        dom_roll = self.dice.roll2d6()
        self.dom_diameter = diameters[dom_roll - 2]
        self.dom_tons = tons[dom_roll - 2]
        max_roll = self.dice.roll1d6()

        if max_roll == 3 and dom_roll < 9:
            self.max_diameter = diameters[7]
            self.max_tons = tons[7]
        elif max_roll == 4 and dom_roll < 11:
            self.max_diameter = "10km"
            self.max_tons = "121 Gt"
        elif max_roll == 5 and dom_roll < 12:
            self.max_diameter = "100km"
            self.max_tons = "21 Tt"
        elif max_roll == 6:
            self.max_diameter = "1000km"
            self.max_tons = "2 Pt"
        else:
            self.max_diameter = self.dom_diameter
            self.max_tons = self.dom_tons
        return

    def generate_zone(self):
        dice_mods = 0
        # TODO depends on Orbit
        # Orbit IS INSIDE -4
        # Orbit IS OUTSIDE +2
        roll = self.dice.roll2d6 + dice_mods
        if roll <= 4:
            self.zone = 'N'
        elif 5 <= roll <= 8:
            self.zone = 'M'
        else:
            self.zone = 'C'
        return

    def generate_composition(self):
        n_zone = [[40, 30, 30], [40, 40, 20], [40, 40, 20], [40, 40, 20], [40, 40, 20], [50, 40, 10], [50, 40, 10],
                  [50, 40, 10], [50, 30, 20], [60, 50, 10], [60, 40, 20]]
        m_zone = [[20, 50, 30], [30, 50, 20], [20, 60, 20], [20, 60, 20], [30, 60, 10], [20, 70, 10], [10, 70, 20],
                  [10, 80, 10], [10, 80, 10], [0, 80, 20], [0, 90, 10]]
        c_zone = [[20, 30, 50], [20, 30, 50], [20, 30, 50], [10, 30, 60], [10, 30, 60], [10, 20, 70], [10, 20, 70],
                  [10, 10, 80], [0, 10, 80], [0, 10, 80], [0, 20, 80]]
        roll = self.dice.roll2d6()
        if self.zone == 'N':
            self.composition = n_zone[roll - 2]
        elif self.zone == 'M':
            self.composition = m_zone[roll - 2]
        elif self.zone == 'C':
            self.composition = c_zone[roll - 2]
        else:
            print("INVALID ZONE")  # TODO replace with exception
        return

    def generate_width(self):
        dice_mods = 0
        if 1 <= self.orbit <= 4:
            dice_mods += -3
        elif 5 <= self.orbit <= 8:
            dice_mods += -1
        elif 9 <= self.orbit <= 12:
            dice_mods += 1
        elif 13 <= self.orbit:
            dice_mods += 3
        else:
            print("INVALID ORBIT")  # TODO replace with exception
        widths = [0.01, 0.05, 0.1, 0.1, 0.5, 0.5, 1.0, 1.5, 2.0, 5.0, 10.0]
        roll = self.dice.roll2d6() + dice_mods
        self.width = widths[roll]
        return

    def generate_belt(self):
        self.generate_diameters()
        self.generate_zone()
        self.generate_composition()
        self.generate_width()

    def output_belt(self):
        beltstring = ""
        if self.max_diameter != self.dom_diameter:
            beltstring += self.dom_diameter + "/" + self.max_diameter + ", "
        else:
            beltstring += self.dom_diameter + ", "
        beltstring += "n-" + self.composition[0] + " m-" + self.composition[1] + " c-" + self.composition[2] + ", "
        beltstring += self.width + "AU"
        return beltstring
