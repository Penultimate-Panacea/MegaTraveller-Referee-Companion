import diceroller


class SocialOutlook:
    def __init__(self, planet, seed):
        self.planet = planet
        self.dice = diceroller(seed)
        self.progressive_attitude = self.generate_progressive_attitude()
        self.progressive_action = self.generate_progressive_action()
        self.aggressive_attitude = None
        self.aggressive_action = None
        self.extensiveness_global = None
        self.extensiveness_intstl = None

    def generate_progressive_attitude(self):
        prog_attitudes = ["Radical", "Radical", "Progressive", "Progressive", "Progressive", "Progressive",
                          "Conservative", "Conservative", "Conservative", 'Conservative', "Reactionary", "Reactionary"]
        dice_mods = 0
        if self.planet.uwp[4] >= 6:
            dice_mods += 1
        if self.planet.uwp[4] >= 9:
            dice_mods += 2
        if self.planet.uwp[6] >= 10:
            dice_mods += 1
        roll = self.dice.roll2d6()
        roll += dice_mods
        if roll > 13:
            index = 13
        else:
            index = roll
        return prog_attitudes[index - 2]

    def generate_progressive_action(self):
        prog_actions = ["Enterprising", "Enterprising", "Enterprising", "Enterprising", "advancing", "Advancing",
                        "Advancing", "Advancing", "Indifferent", "Indifferent", "Indifferent", "Stagnant"]
        dice_mods = 0
        if self.progressive_attitude == "Conservative":
            dice_mods += 3
        elif self.progressive_attitude == "Reactionar":
            dice_mods += 6
        if self.planet.uwp[6] >= 10:
            dice_mods += 1
        roll = self.dice.roll2d6()
        roll += dice_mods
        if roll > 13:
            index = 13
        else:
            index = roll
        return prog_actions[index - 2]
