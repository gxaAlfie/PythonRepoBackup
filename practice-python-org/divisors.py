input_number = int(input('Number to divide: '))

for num in range(1, input_number):
    print(num) if (input_number % num == 0) else next

# List comprehension
# [ print(num) for num in range(1, input_number) if (input_number % num == 0) ]
