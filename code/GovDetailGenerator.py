class GovernmentDetails:
    def __init__(self, planet, seed):
        self.planet = planet
        self.dice = DiceRoller(seed)
        self.representative_authority_org_type = self.determine_respresentative_authority_org_type()
        self.representative_authority_branch = None  # handled via generate_other_authorities()
        self.other_authorities = None  # handled via generate_other_authorities()
        self.executive = self.generate_other_authorities()
        self.judicial = self.generate_other_authorities()
        self.legislative = self.generate_other_authorities()
        self.generate_other_authorities()

    def generate_representative_authority(self):
        orgs = ["Democracy", "Elite Council", "Elite Council", "Elite Council", "Ruler", "Ruler", "Several Councils",
                "Several Councils", "Several Councils", "Several Councils", "Democracy"]
        org_roll = self.dice.roll2d6()
        return orgs[org_roll - 2]

    def handle_balkanized(self):
        # TODO THIS
        return

    def determine_respresentative_authority_org_type(self):
        if self.planet.uwp[5]  == 0:
            return "No authority"
        elif self.planet.uwp[5] == 1:
            return self.generate_representative_authority()
        elif self.planet.uwp[5] == 2:
            return "Democracy"
        elif self.planet.uwp[5] == 3:
            roll = self.dice.roll1d6()
            if roll < 5:
                return "Elite Council"
            else:
                return "Several Councils"
        elif 3 < self.planet.uwp[5] < 7:
            return self.generate_representative_authority()
        elif self.planet.uwp[5] == 7:
            return self.handle_balkanized()
        elif self.planet.uwp[5] == 8 or 9:
            return "Several Councils"
        elif self.planet.uwp[5] == 10:
            roll = self.dice.roll1d6()
            if roll < 6:
                return "Ruler"
            else:
                return "Elite Council"
        elif self.planet.uwp[5] == 11:
            roll = self.dice.roll1d6()
            if roll < 6:
                return "Ruler"
            else:
                return "Elite Council"
        elif self.planet.uwp[5] == 12:
            roll = self.dice.roll1d6()
            if roll < 5:
                return "Elite Council"
            else:
                return "Several Councils"
        elif self.planet.uwp[5] == 13:
            result = self.generate_representative_authority()
            while result == "Democracy":
                result = self.generate_representative_authority()
            return result
        elif self.planet.uwp[5] == 14:
            result = self.generate_representative_authority()
            while result == "Democracy":
                result = self.generate_representative_authority()
            return result
        elif self.planet.uwp[5] == 15:
            roll = self.dice.roll1d6()
            if roll < 5:
                return "Elite Council"
            else:
                return "Several Councils"

    def generate_other_authorities(self):
        splits = [3, 3, 2, 2, 1, 1]
        split_roll = self.dice.roll1d6()
        split = splits[split_roll - 1]
        if split == 1:
            return "No other authorities"
        elif split == 2:
            two_ways = [["Executive & Judicial", "Legislative"], ["Executive & Judicial", "Legislative"],
                        ["Executive & Legislative", "Judicial"], ["Executive & Legislative", "Judicial"],
                        ["Executive & Legislative", "Judicial"], ["Legislative & Judical", "Executive"]]
            two_way_roll = self.dice.roll1d6()
            two_way = two_ways[two_way_roll - 1]
            self.representative_authority_branch = two_way[0]
            self.other_authorities = two_way[1]
            return
        elif split == 3:
            three_ways = [["Executive", "Legislative & Judicial"], ["Executive", "Legislative & Judicial"],
                          ["Legislative", "Executive & Judicial"], ["Legislative", "Executive & Judicial"],
                          ["Judicial", "Executive & Legislative"], ["Judicial", "Executive & Legislative"]]
            three_way_roll = self.dice.roll1d6()
            three_way = three_ways[three_way_roll - 1]
            self.representative_authority_branch = three_way[0]
            self.other_authorities = three_way[1]
