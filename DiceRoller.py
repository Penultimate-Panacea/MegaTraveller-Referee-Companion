import random
class DiceRoller:
    def __init__(self, uniqueSeed):
        random.seed(uniqueSeed, 2)

    def roll1D6(self):
        roll = random.randint(1,6)
        return roll

    def rollD3(self):
        roll =random.randint(1,6) % 3
        return roll

    def roll2D6(self):
        result1 = self.roll1D6()
        result2 = self.roll1D6()
        roll = result1 + result2
        return roll

    def rollND6(self, n):
        i = 0
        roll = 0
        while n > i:
            roll += self.roll1D6()
            i += 1
        return roll

    def rollD66(self):
        result1 = random.randint(1,6)
        result2 = random.randint(1,6)
        roll = [result1, result2]
        return roll


