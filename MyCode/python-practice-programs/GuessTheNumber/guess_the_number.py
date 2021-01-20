from random import randint
import argparse, pdb

def main(random_number):
    while True:
        closeness = check_proximity(input("Guess: "))
        if closeness == 0:
            print("You got the number!")
            break
        else if closeness == 1:
            print("Number is Smaller.")
        else if closeness == -1:
            print("Number is Larger.")
        else:
            print("Invalid Input!")
    
def check_and_get_integer(number):
    try:
        return int(number)
    except ValueError:
        return None

def check_proximity(number):
    if number = check_and_get_integer(number):
        return number > 


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("max_range", type=int, help="Maximum Range of Number To Guess From")
    parser.add_argument("-min", "--min_range", type=int, help="Minimum Range of Number To Guess From", default=1)
    return parser.parse_args()

def get_random_number(min_num, max_num):
    return randint(min_num, max_num)

if __name__ == "__main__":
    parsed_arguments = parse_arguments()
    random_number    = get_random_number(parsed_arguments.min_range, parsed_arguments.max_range)
    main(random_number)
