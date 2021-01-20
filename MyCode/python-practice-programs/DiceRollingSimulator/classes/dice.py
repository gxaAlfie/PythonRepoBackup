from random import randint
from modules.number_format import get_integer

class Dice(object):
    def __init__(self, num_of_sides):
        self._sides = get_integer(num_of_sides)

    def roll(self):
        dice_roll = randint(1, self._sides)
        print(f"Rolling {self._sides}-sided die rolls: {dice_roll}")
