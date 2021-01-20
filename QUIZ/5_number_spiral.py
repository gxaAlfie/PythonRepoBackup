from sys import argv
from itertools import cycle

number_to_spiral  = int(argv[1])
max_number_spiral = number_to_spiral**2 - 1
range_spiral      = range(0, number_to_spiral)

spiral_matrix     = [ [0 for x in range_spiral] for y in range_spiral ]

x,y = [0,0]
condition_loop    = cycle(range(1,5))
current_condition = condition_loop.next()

def check_condition(curr_x, curr_y, current_condition):
    condition_dict = {
        1: (curr_y+1 < number_to_spiral and spiral_matrix[curr_x][curr_y+1] == 0),
        2: (curr_x+1 < number_to_spiral and spiral_matrix[curr_x+1][curr_y] == 0),
        3: (curr_y-1 >= 0 and spiral_matrix[curr_x][curr_y-1] == 0),
        4: (curr_x-1 >= 0 and spiral_matrix[curr_x-1][curr_y] == 0)
    }
    return condition_dict[current_condition]

def update_x_y(new_x, new_y, current_condition):
    action_dict = {
        1: [new_x,new_y+1],
        2: [new_x+1,new_y],
        3: [new_x,new_y-1],
        4: [new_x-1,new_y]
    }
    return action_dict[current_condition]

for number in range(max_number_spiral, -1, -1):
    spiral_matrix[x][y] = number
    if not check_condition(x,y,current_condition):
        current_condition = condition_loop.next()
    x,y = update_x_y(x,y, current_condition)

for x in range_spiral:
    for y in range_spiral:
        print "{0}\t".format(spiral_matrix[x][y]),
    print "\n"
