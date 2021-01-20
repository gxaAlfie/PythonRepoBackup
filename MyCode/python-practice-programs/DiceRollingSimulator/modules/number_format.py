def get_integer(number):
    try:
        return int(number)
    except ValueError:
        print("\nNot a valid number.\n")
        return 0
