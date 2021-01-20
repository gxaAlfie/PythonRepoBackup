# Program demonstrates more file reading and writing techniques

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to about."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()

# "with" will also close the file "correctly", said to be better than explicit close
# can be written as:
# with open(from_file) as in_file:
#   indata = in_file.read()
#
# with open(to_file, 'w') as out_file:
#   out_file.write(indata)
