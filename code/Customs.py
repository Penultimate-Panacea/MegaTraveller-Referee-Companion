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

    def generate_dressing_habits(self):
        dressing_habits_0 = ["Same clothes for all sexes",
                             "Unusual clothes for " + self.generate_practicing_group(),
                             "Unusual clothes for " + self.generate_practicing_group(),
                             "Unusual clothes for " + self.generate_practicing_group(),
                             "Unusual headgear for " + self.generate_practicing_group(),
                             "Unusual headgear for " + self.generate_practicing_group()]
        dressing_habits_1 = ["Shaved heads for " + self.generate_practicing_group(),
                             "Shaved heads for " + self.generate_practicing_group(),
                             "Hair never cut " + self.generate_practicing_group(),
                             "Hair never cut " + self.generate_practicing_group(),
                             "Unusual hair color for " + self.generate_practicing_group(),
                             "Unusual hair color for " + self.generate_practicing_group()]
        dressing_habits_2 = ["Unusual hairdos for " + self.generate_practicing_group(),
                             "Unusual hairdos for " + self.generate_practicing_group(),
                             "Unusual hairdos for " + self.generate_practicing_group(),
                             "Unusual eyebrows for " + self.generate_practicing_group(),
                             "Unusual facial alterations for " + self.generate_practicing_group(),
                             "Unusual body alternations for " + self.generate_practicing_group()]
        dressing_habits_3 = ["Unusual fingernails for " + self.generate_practicing_group(),
                             "Unusual fingernails for " + self.generate_practicing_group(),
                             "Unusual toenails for " + self.generate_practicing_group(),
                             "Unusual toenails for " + self.generate_practicing_group(),
                             "Unusual cosmetics for " + self.generate_practicing_group(),
                             "Unusual cosmetics for " + self.generate_practicing_group()]
        dressing_habits_4 = ["Unusual cosmetics for " + self.generate_practicing_group(),
                             "Unusual jewelery for " + self.generate_practicing_group(),
                             "Unusual jewelery for " + self.generate_practicing_group(),
                             "Unusual jewelery for " + self.generate_practicing_group(),
                             "Unusual accessories for " + self.generate_practicing_group(),
                             "Unusual accessories for " + self.generate_practicing_group()]
        dressing_habits_5 = ["Unusual handgear for " + self.generate_practicing_group(),
                             "Unusual handgear for " + self.generate_practicing_group(),
                             "Tatooing on face for " + self.generate_practicing_group(),
                             "Tatooing on body for " + self.generate_practicing_group(),
                             "Tatooing on body for " + self.generate_practicing_group(),
                             "Hidden tatooing for " + self.generate_practicing_group()]
        dressing_habits_lol = [dressing_habits_0, dressing_habits_1, dressing_habits_2, dressing_habits_3,
                               dressing_habits_4, dressing_habits_5]
        roll1 = self.dice.roll_1d6() - 1
        roll2 = self.dice.roll_1d6() - 1
        chosen_dressing_habit = dressing_habits_lol[roll1][roll2]
        return chosen_dressing_habit

    def generate_eating_habits(self):
        eating_habits_0 = ["Unusual foods for " + self.generate_practicing_group(),
                           "Unusual foods for " + self.generate_practicing_group(),
                           "Unusual beverages for " + self.generate_practicing_group(),
                           "Unusual beverages for " + self.generate_practicing_group(),
                           "Unusual food preparation for " + self.generate_practicing_group(),
                           "Unusual food preparation for " + self.generate_practicing_group()]
        eating_habits_1 = [self.generate_practicing_group() + " are segregated during meals",
                           self.generate_practicing_group() + " are segregated during meals",
                           self.generate_practicing_group() + " are vegetarians",
                           self.generate_practicing_group() + " are vegetarians",
                           self.generate_practicing_group() + " are carnivorous",
                           self.generate_practicing_group() + " are carnivorous"]
        eating_habits_2 = [self.generate_practicing_group() + " are omnivorous",
                           self.generate_practicing_group() + " are omnivorous",
                           "Certain colored food taboo for " + self.generate_practicing_group(),
                           "Certain colored food taboo for " + self.generate_practicing_group(),
                           "Certain shaped food taboo for " + self.generate_practicing_group(),
                           "Certain food sources taboo for " + self.generate_practicing_group()]
        eating_habits_3 = [self.generate_practicing_group() + " eats in special location",
                           self.generate_practicing_group() + " eats only in private",
                           self.generate_practicing_group() + " eats in a special orientation",
                           self.generate_practicing_group() + " eats with unusual utensils",
                           self.generate_practicing_group() + " only eats at home",
                           self.generate_practicing_group() + " only eats at home"]
        eating_habits_4 = [self.generate_practicing_group() + " eat at unusual times",
                           self.generate_practicing_group() + " eat at unusual times",
                           self.generate_practicing_group() + " eat only certain times",
                           self.generate_practicing_group() + " eat only certain ways",
                           "Rituals before eating for " + self.generate_practicing_group(),
                           "Rituals after eating for " + self.generate_practicing_group()]
        eating_habits_5 = ["One sex eats the other's leftovers", 
                           "One age eats the other's leftovers",
                           self.generate_practicing_group() + " eats the " + self.generate_practicing_group() +
                           " leftovers",
                           "One class eats the other's leftovers",
                           "One race eats the others leftovers",
                           self.generate_practicing_group() + " are cannibalistic"]
        eating_habits_lol = [eating_habits_0, eating_habits_1, eating_habits_2, eating_habits_3, eating_habits_4,
                             eating_habits_5]
        roll1 = self.dice.roll_1d6() - 1
        roll2 = self.dice.roll_1d6() - 1
        chosen_eating_habit = eating_habits_lol[roll1][roll2]
        return chosen_eating_habit
