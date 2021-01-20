import os, datetime

class FileSave(object):
    def __init__(self, items):
        self._total_items = items.pop('total')
        self._items_to_save_dict = items

    def save_items_to_file(self):
        get_current_date_string = datetime.datetime.now().strftime("%Y-%m-%d")
        with open('laundry_list.txt', 'w') as file:
            file.write("Laundry List for %s\n\n" % get_current_date_string)

            for item, count in self._items_to_save_dict.iteritems():
                file.write("%s x %d\n" % (item,count))

            file.write("\nTotal: %d" % self._total_items)
