from classes.dice import Dice
from classes.dice_number_validator import DiceNumberValidator

class DiceHolder(object):
    def __init__(self):
        self._dice = []

    def add_dice(self, num_of_sides):
        if DiceNumberValidator(num_of_sides).validate():
            self._dice.append(Dice(num_of_sides))

    def roll_dice(self):
        if self.any_dice():
            for dice in self._dice:
                dice.roll()
        else:
            print("\nNo Dice.\n")

    def any_dice(self):
        return len(self._dice) != 0


