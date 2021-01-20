from sys import argv

numbers = argv[1:]
unique_numbers = set(numbers)

if len(unique_numbers) != len(numbers):
    print "Array has duplicated elements"
else:
    print "Array has unique elements"
