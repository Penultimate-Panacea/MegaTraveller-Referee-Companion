class Religion:
    def __init__(self, planet, seed):
        self.planet = planet
        self.dice = diceroller(seed)
        self.god_view = None
        self.spiritual_view = None
        self.devotion = None
        self.organization = None
        self.formality = None
        self.fervor = None
        self.adherents = None
        self.profile = None  # Maybe this should be a toString style function?

    # TODO Generate God View
