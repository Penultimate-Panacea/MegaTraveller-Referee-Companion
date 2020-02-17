import diceroller


class SocialOutlook:
    def __init__(self, planet, seed):
        self.planet = planet
        self.dice = diceroller(seed)
        self.progressive_attitude = self.generate_progressive_attitude()
        self.progressive_action = self.generate_progressive_action()
        self.aggressive_attitude = self.generate_aggressive_attitude()
        self.aggressive_action = self.generate_aggresive_action()
        self.extensiveness_globe = self.generate_extensiveness_globe()
        self.extensiveness_intstl = self.generate_extensiveness_intstl()

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

    def generate_aggressive_attitude(self):
        agg_attitute = ["Expansionistic", "Expansionistic", "Competitve", "Competetive", "Competetive", "Unaggressive",
                        "Unaggressive", "Unaggressive", "Unaggressive", "Passive", "Passive", "Passive"]
        dice_mods = 0
        if self.planet.uwp[6] >= 10:
            dice_mods += 1
        roll = self.dice.roll2d6()
        roll += dice_mods
        if roll > 13:
            index = 13
        else:
            index = roll
        return agg_attitute[index - 2]

    def generate_aggresive_action(self):
        agg_action = ["Militant", "Militant", "Militant", "Neutral", "Neutral", "Neutral", "Neutral", "Peaceable",
                      "Peaceable", "Peaceable", "Conciliatory", "Conciliatory"]
        dice_mods = 0
        if self.aggressive_attitude == "Expansionistic":
            dice_mods -= 2
        elif self.aggressive_attitude == "Competitive":
            dice_mods -= 1
        elif self.aggressive_attitude == "Passive":
            dice_mods += 2
        if self.planet.uwp[6] >= 10:
            dice_mods += 1
        roll = self.dice.roll2d6()
        roll += dice_mods
        if roll > 13:
            index = 13
        else:
            index = roll
        return  agg_action[index - 2]

    def generate_extensiveness_globe(self):
        globe = ["Monolithic", "Monolithic", "Harmonious", "Harmonious", "Harmonious", "Harmonious", "Discordant",
                 "Discordant", "Discordant", "Discordant", "Fragmented", "Fragmented"]
        dice_mods = 0
        if self.planet.uwp[5] < 3:
            dice_mods += 1
        elif self.planet.uwp[5] == 7:
            dice_mods += 4
        elif self.planet.uwp[5] == 15:
            dice_mods -= 1
        if self.aggressive_attitude == "Passive":
            dice_mods += 2
        if self.planet.uwp[6] < 5:
            dice_mods += 1
        elif self.planet.uwp[6] > 9:
            dice_mods -= 1
        roll = self.dice.roll2d6()
        roll += dice_mods
        if roll > 13:
            index = 13
        elif roll < 2:
            index = 2
        else:
            index = roll
        return globe[index -2]

    def generate_extensiveness_intstl(self):
        interstellar = ["Xenophillic", "Xenophillic", "Friendly", "Friendly", "Friendly", "Friendly", "Aloof", "Aloof",
                        "Aloof", "Aloof", "Xenophobic", "Xenophobic"]
        dice_mods = 0
        if self.planet.uwp[0] == 'A':
            dice_mods -= 2
        elif self.planet.uwp[0] == 'B':
            dice_mods -= 1
        elif self.planet.uwp[0] == 'D':
            dice_mods += 1
        elif self.planet.uwp[0] == 'E':
            dice_mods += 2
        elif self.planet.uwp[0] == 'X':
            dice_mods += 3
        if self.progressive_attitude == "Conservative":
            dice_mods += 2
        elif self.progressive_attitude == "Reactionary":
            dice_mods += 4
        if self.planet.uwp[6] > 9:
            dice_mods += 1
        roll = self.dice.roll2d6()
        roll += dice_mods
        if roll > 13:
            index = 13
        elif roll < 2:
            index = 2
        else:
            index = roll
        return interstellar[index - 2]