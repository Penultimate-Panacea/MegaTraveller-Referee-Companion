import diceroller


class GovernmentDetails:
    def __init__(self, planet, seed):
        self.planet = planet
        self.dice = diceroller(seed)
        self.representative_authority = self.determine_respresentative_authority()
        self.other_authorities = None

    def generate_representative_authority(self):
        orgs = ["Democracy", "Elite Council", "Elite Council", "Elite Council", "Ruler", "Ruler", "Several Councils",
                "Several Councils", "Several Councils", "Several Councils", "Democracy"]
        org_roll = self.dice.roll2d6()
        return orgs[org_roll - 2]

    def handle_balkanized(self):
        # TODO THIS
        return

    def determine_respresentative_authority(self):
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
        elif self.planet.uwp[5] == 14
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

