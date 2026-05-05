class Game:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        score = 0
        roll_index = 0

        for frame in range(10):
            if self.is_strike(roll_index):
                score += 10 + self.strike_bonus(roll_index)
                roll_index += 1
            elif self.is_spare(roll_index):
                score += 10 + self.spare_bonus(roll_index)
                roll_index += 2
            else:
                score += self.sum_of_balls(roll_index)
                roll_index += 2

        return score

    def is_strike(self, i):
        return self.rolls[i] == 10

    def is_spare(self, i):
        return self.rolls[i] + self.rolls[i + 1] == 10

    def strike_bonus(self, i):
        return self.rolls[i + 1] + self.rolls[i + 2]

    def spare_bonus(self, i):
        return self.rolls[i + 2]

    def sum_of_balls(self, i):
        return self.rolls[i] + self.rolls[i + 1]