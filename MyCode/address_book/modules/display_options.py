GENERAL_OPTIONS = {
    1: "add_person",
    2: "edit_person",
    3: "remove_person",
    4: "show_people",
    5: "exit"
}

SEARCH = {
    1: 'search_by_name',
    2: 'search_by_number',
    3: 'search_by_address'
}

def display_options(options_dict):
    for key, action in options_dict.iteritems():
        print "[%d] %s" % (key, action.replace("_", " ").capitalize())
