from content_validator import ContentValidator

class LaundryList(object):
    GENERAL_FUNCTIONS = {1: "add_item", 2: "show_items", 3: "exit"}

    def __init__(self):
        self._laundry_list = {}

    def total_items(self):
        print "Total: %s" % sum(self._laundry_list.values())

    def add_item(self):
        while True:
            item = raw_input('Item: ')
            quantity = raw_input('Quantity: ')
            if (item != "" or quantity != "") and (ContentValidator.check_valid_and_whole_num(quantity)):
                self._laundry_list[item] = int(quantity)
            else:
                print "Not a valid input"
            if 'n' == raw_input("Press n to stop or other key to continue): "):
                break


    def show_items(self):
        for item, count in self._laundry_list.iteritems():
            print "%s x %d" % (item, count)
        self.total_items()

    def get_laundry_items(self):
        total_dict = {"total": sum(self._laundry_list.values())}
        return dict(self._laundry_list, **total_dict)

    @classmethod
    def display_options(self, options_dict):
        for key, action in options_dict.iteritems():
            print "[%d] %s" % (key, action.replace("_", " ").capitalize())
