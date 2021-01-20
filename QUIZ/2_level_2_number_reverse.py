from sys import argv

dimensions = int(argv[1])
squared_count = (dimensions ** 2)-1

for i in range(squared_count, -1, -1):
    print i,
    if i % dimensions == 0: print "\n"
