from classes.dice_holder import DiceHolder

def main(dice_holder):
    while True:
        print("[1] Add Dice")
        print("[2] Roll Dice")
        print("[3] Exit")
        user_input = input("Option: ")
        if user_input == "1":
            dice_holder.add_dice(input("How many sides: "))
        elif user_input == "2":
            dice_holder.roll_dice()
        elif user_input == "3":
            break
        else:
            print("Not an Option.\n")
        
if __name__ == "__main__":
    main(DiceHolder())
