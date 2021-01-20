max_number = int(input("Display Numbers Less Than: "))

initial_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for num in initial_list: next if num >= max_number else print(num)

# List comprehension answer
# [print(num) for num in initial_list if num < max_number]
