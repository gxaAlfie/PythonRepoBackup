from classes.content_validator import ContentValidator
from classes.laundry_list import LaundryList
from classes.file_saver import FileSave

def main():
    laundry_list = LaundryList()
    while True:
        LaundryList.display_options(LaundryList.GENERAL_FUNCTIONS)
        option = raw_input('Select Option: ')
        if ContentValidator.check_valid_num(option):
            option = int(option)
            if option not in LaundryList.GENERAL_FUNCTIONS.keys():
                print "NOT AN OPTION"
            else:
                if option == 3:
                    file_saver = FileSave(laundry_list.get_laundry_items())
                    file_saver.save_items_to_file()
                    break
                else:
                    method_name = LaundryList.GENERAL_FUNCTIONS[option]
                    method      = getattr(laundry_list, method_name)
                    method()
        else:
            print "INPUT IS NOT A NUMBER"

"""
This part is important
because if you use this as a module and import this file to another file
it should not run main() since this file "my_laundry_list" is not the main program
"""
if __name__=="__main__":
    main()
