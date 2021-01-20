from sys import argv

multiplication_table_size = int(argv[1])+1
table_range               = range(1,multiplication_table_size)

for i in table_range:
    for y in table_range:
        print i*y,
    print "\n"
