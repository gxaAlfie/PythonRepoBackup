from sys import argv
from string import ascii_uppercase

string_to_count = argv[1].upper()

letter_counter_dict = {letter: string_to_count.count(letter) for letter in ascii_uppercase}
for (key,value) in letter_counter_dict.iteritems(): print "{0}: {1}".format(key, value)
