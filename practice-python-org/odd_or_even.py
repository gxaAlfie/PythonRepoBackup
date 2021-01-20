def multiple_of(input_multiple, input_number):
    return input_number % multiple == 0

def is_even(input_number):
    return input_number % 2 == 0

number = int(input("Your number: "))
multiple = int(input("Number to divide by: "))

if multiple_of(multiple, number):
    print("It's multiple of " + str(multiple))
elif is_even(number):
    print("It's even.")
else:
    print("It's odd.")

# Initial Solution
# print("It's even." if is_even(number) else "It's odd.")
