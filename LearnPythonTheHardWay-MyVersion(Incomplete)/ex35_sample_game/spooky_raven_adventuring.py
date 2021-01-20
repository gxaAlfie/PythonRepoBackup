#from classes.player import Player
from classes.manor import Manor
from modules.prologue import *

def main():
    while True:
        start = prologue()
        if start == "1":
            manor = Manor()
            manor.go_to_entrance()
            while True:
                manor.lobby_rooms()
                room_to_enter = raw_input("\t> ")
                break
            break

        elif start == "2":
            print "\tYou beat a hasty retreat."
            break
        else:
            print "\tThat's not a possible option"



if __name__ == '__main__':
    main()
