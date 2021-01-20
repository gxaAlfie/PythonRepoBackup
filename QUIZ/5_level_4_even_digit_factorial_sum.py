from sys import argv
from math import factorial

factorial_number = int(argv[1])

factorial_even_number_list = [int(number) for number in str(factorial(factorial_number)) if int(number) % 2 == 0]
print sum(factorial_even_number_list)
