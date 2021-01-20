input_list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
input_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

output = []

for num1 in input_list1:
    if num1 in input_list2 and num1 not in output:
        output.append(num1)

print(output)
