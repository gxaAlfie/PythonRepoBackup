from person import Person
from modules.content_validator import *
from modules.display_options import *

class PersonList(object):
    def __init__(self):
        self._list = []

    def add_person(self):
        person = self.setup_person()
        self._list.append(person)
        print "ADDED PERSON TO LIST"

    def setup_person(self):
        my_details = {}
        my_details['name'] = raw_input('Name: ')
        my_details['number'] = raw_input('Phone Number: ')
        my_details['address'] = raw_input('Address: ')
        return Person(my_details)

    def edit_person(self):
        display_options(SEARCH)
        option = raw_input('Select Option: ')
        if check_valid_num(option):
            option = int(option)
            if option not in SEARCH.keys():
                print "NOT AN OPTION"
            else:
                query = raw_input("Text to Search: ")
                matching_item = self.find_person(option, query)
                if not isinstance(matching_item, None.__class__):
                    person = self._list.pop(matching_item[1])
                    person._name = raw_input('Name: ')
                    person._address = raw_input('Address: ')
                    person._number = raw_input('Phone Number: ')
                    self._list.append(person)
                    print "PERSON UPDATED"
                else:
                    print "NO PERSON FOUND"
        else:
            print "INPUT IS NOT A NUMBER"

    def remove_person(self):
        display_options(SEARCH)
        option = raw_input('Select Option: ')
        if check_valid_num(option):
            option = int(option)
            if option not in SEARCH.keys():
                print "NOT AN OPTION"
            else:
                query = raw_input("Text to Search: ")
                matching_item = self.find_person(option, query)
                if not isinstance(matching_item, None.__class__):
                    self._list.pop(matching_item[1])
                    print "PERSON REMOVED"
                else:
                    print "NO PERSON FOUND"
        else:
            print "INPUT IS NOT A NUMBER"

    def show_people(self):
        print "ADDRESS BOOK"
        if len(self._list) == 0:
            print "EMPTY\n"
        else:
            for item in self._list:
                item.show_details()

    def find_person(self, finding_condition, param):
        if finding_condition == 1:
            attribute = "_name"
        elif finding_condition == 2:
            attribute = "_number"
        else:
            attribute = "_address"
        return self.search(param.lower(), attribute)

    def search(self, param, attribute):
        match_item = next(((item, index) for index,item in enumerate(self._list) if getattr(item, attribute).lower().find(param) != -1), None)
        return match_item
