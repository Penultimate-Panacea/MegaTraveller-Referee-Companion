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


