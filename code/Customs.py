import diceroller


class Customs:
    def __init__(self, planet, seed):
        self.planet = planet
        self.dice = diceroller(seed)
        self.customs = None

    def generate_practicing_group(self):
        group0 = ["Certain political groups", "Certain political groups", "Certain geographic regions",
                  "Certain geographic regions", "Certain sex", "Certain sex"]
        group1 = ["Certain sex", "Enforcement figures", "Entertainment figures", "Heroic Figures", "Athletic Figures",
                  "Certain races"]
        group2 = ["Certain races", "Certain races", "Religious figure", "Religious figures", "Military figures",
                  "Military figures"]
        group3 = ["Certain occupations", "Certain occupations", "Political figures", "Political figures",
                  "Medical figures", "Medical figures"]
        group4 = ["Certain age groups", "Certain age groups", "Scientific figures", "Scientific figures",
                  "Academic figures", "Academic figures"]
        group5 = ["Low social class", "Low social class", "High social class", "High social class",
                  "Convicted criminals", "Convicted criminals"]
        groups = [group0, group1, group2, group3, group4, group5]
        roll0 = self.dice.roll_1d6()
        roll1 = self.dice.roll_1d6() - 1
        roll2 = self.dice.roll_1d6() - 1
        if roll0 < 4:
            chosen_group = "The entire population"
        else:
            chosen_group = groups[roll1][roll2]
        return chosen_group

