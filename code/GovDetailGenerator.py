import diceroller


class GovernmentDetails:
    def __init__(self, planet, seed):
        self.planet = planet
        self.dice = diceroller(seed)
        self.representative_authority = self.determine_respresentative_authority()
        self.other_authorities = None


