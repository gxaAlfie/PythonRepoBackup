from classes.person_list import PersonList
from modules.content_validator import *
from modules.display_options import *

def main():
    address_book = PersonList()
    while True:
        display_options(GENERAL_OPTIONS)
        option = raw_input('Select Option: ')

        if check_valid_num(option):
            option = int(option)
            if option not in GENERAL_OPTIONS.keys():
                print "NOT AN OPTION"
            else:
                if option == 5:
                    break
                else:
                    method_name = GENERAL_OPTIONS[option]
                    method      = getattr(address_book, method_name)
                    method()
        else:
            print "INPUT IS NOT A NUMBER"

if __name__ == '__main__':
    main()
