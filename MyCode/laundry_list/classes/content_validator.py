class ContentValidator(object):
    @classmethod
    def check_valid_and_whole_num(self, num):
        try:
            if int(num) >= 0:
                return True
        except ValueError:
            return False

    @classmethod
    def check_valid_num(self, num):
        try:
            int(num)
            return True
        except ValueError:
            return False
