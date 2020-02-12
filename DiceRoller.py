import random
class DiceRoller(seed):
    def rollD6():
        roll = random.randint(1,6)
        return roll

    def rollD3():
        roll =random.randint(1,6) % 3
        return roll

    def roll2D6():
        result1 = rollD6()
        result2 = rollD6()
        roll = result1 + result2
        return roll

    def rollD66():
        result1 = random.randint(1,6)
        result2 = random.randint(1,6)
        roll = [result1, result2]
        return roll
