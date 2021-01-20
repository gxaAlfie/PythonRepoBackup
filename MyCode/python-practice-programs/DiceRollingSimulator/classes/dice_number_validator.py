from modules.number_format import get_integer

class DiceNumberValidator(object):
    def __init__(self, number):
        self._num_of_sides = get_integer(number)

    def is_greater_than_equal_to_one(self):
        return self._num_of_sides >= 1

    def validate_number(validate_function):
        def wrapper(self):
            if self.is_greater_than_equal_to_one():
                return validate_function()
        return wrapper

    @validate_number
    def validate():
        return True
