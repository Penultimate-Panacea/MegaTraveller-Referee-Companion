import diceroller


class Planet:
    def __init__(self):
        self.uwp = ["X", 0, 0, 0, 0, 0, 0, 0]  # default
        self.size_details = None
        self.atmo_details = None
        self.hydr_details = None
        self.pops_details = None
        self.govt_details = None
        self.lawl_details = None
        self.tech_details = None
        self.name = None
        self.dice = diceroller(self.name)
        self.orbit = None  # This may be the wrong way to do this

    def mainworld_basic_gen(self):
        backwater_starport = ['A', 'A', 'B', 'B', 'C', 'C', 'C', 'D', 'E', 'E', 'X']
        standard_starport = ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'D', 'E', 'E', 'X']
        mature_starport = ['A', 'A', 'A', 'B', 'B', 'C', 'C', 'D', 'E', 'E', 'E']
        cluster_starport = ['A', 'A', 'A', 'A', 'B', 'B', 'C', 'C', 'D', 'E', 'X']
        starport_roll = self.dice.roll2d6() - 2
        self.uwp[0] = standard_starport[starport_roll] # TODO autoselect of starport table
        self.uwp[1] = self.dice.roll2d6() - 2
        if self.uwp[1] == 0:
            self.uwp[2] = 0
        else:
            self.uwp[2] = self.dice.roll2d6() - 7 + self.uwp[1]
        if self.uwp[1] < 2:
            self.uwp[3] = 0
        elif self.uwp[2] < 2 or self.uwp[2] > 9:
            self.uwp[3] = self.dice.roll2d6() + self.uwp[1] - 7 - 4
        else:
            self.uwp[3] = self.dice.roll2d6() + self.uwp[1] - 7
        self.uwp[4] = self.dice.roll2d6() - 2
        self.uwp[5] = self.dice.roll2d6() + self.uwp[4] - 7
        self.uwp[6] = self.dice.roll2d6() + self.uwp[5] - 7
        self.uwp[7] = self.basic_tech_gen()

    def basic_tech_gen(self):
        dice_mods = 0
        if self.uwp[0] == 'A':
            dice_mods += 6
        elif self.uwp[0] == 'B':
            dice_mods += 4
        elif self.uwp[0] == 'C':
            dice_mods += 2
        elif self.uwp[0] == 'X':
            dice_mods += -4
        elif self.uwp[1] == 0 or 1:
            dice_mods += 2
        elif self.uwp[1] == 2 or 3 or 4:
            dice_mods += 1
        elif 0 <= self.uwp[2] <= 3:
            dice_mods += 1
        elif self.uwp[2] > 9:
            dice_mods += 1
        elif self.uwp[3] == 9:
            dice_mods += 1
        elif self.uwp[3] == 10:
            dice_mods += 2
        elif 0 < self.uwp[4] < 6:
            dice_mods += 1
        elif self.uwp[4] == 9:
            dice_mods += 2
        elif self.uwp[4] == 10:
            dice_mods += 4
        elif self.uwp[5] == 0 or 5:
            dice_mods += 1
        elif self.uwp[5] == 13:
            dice_mods += -2
        tech_level = self.dice.roll1d6() + dice_mods
        return tech_level

class GasGiant:
    def __init__(self):
        self.size_details = None
        self.atmo_details = None
        self.hydr_details = None
        self.pops_details = None
        self.govt_details = None
        self.lawl_details = None
        self.name = None
