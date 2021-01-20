class Person(object):
    def __init__(self, details):
        self._name = details['name']
        self._number = details['number']
        self._address = details['address']

    def show_details(self):
        print "---------------------------"
        print "Name: ", self._name
        print "Phone Number: ", self._number
        print "Address: ", self._address
        print "---------------------------\n"
