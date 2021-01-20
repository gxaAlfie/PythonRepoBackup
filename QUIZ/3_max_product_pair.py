from operator import mul
from sys import argv

sorted_numbers  = sorted(map(int, argv[1:]))
print reduce(mul, sorted_numbers[-2:])
