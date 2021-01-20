def check_valid_and_whole_num(num):
    try:
        if int(num) >= 0:
            return True
    except ValueError:
        return False

def check_valid_num(num):
    try:
        int(num)
        return True
    except ValueError:
        return False
