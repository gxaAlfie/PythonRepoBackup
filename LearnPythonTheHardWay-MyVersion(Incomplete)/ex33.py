# Program demonstrates while loops

i = 0
my_numbers = []

while i < 6:
    print "At the top i is %d" % i
    my_numbers.append(i)

    i+=1
    print "Numbers now: ", my_numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in my_numbers:
    print num
