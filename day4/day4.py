##########################################################################
# STEP 1 OF 2
##########################################################################

import os
directory = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory, "input.txt")

with open(filepath, 'r') as file:
    grid = [list(line.strip()) for line in file]

def sum_tuples(a,b):
    if len(a) != len(b):
        print("Error")
        return None
    else:
        return tuple(a[i] + b[i] for i in range(len(a)))
    
def sub_tuples(b,a):
    if len(a) != len(b):
        print("Error")
        return None
    else:
        return tuple(b[i] - a[i] for i in range(len(a)))

def read(grid, substring, current_position, next_position):
    # [line][column]

    # Exit condition
    line = current_position[0]
    column = current_position[1]

    if line < 0 or line >= len(grid):
        return 0
    if column < 0 or column >= len(grid[line]):
        return 0

    current_letter = grid[line][column]

    # Exit condition
    if current_letter != substring[0]:
        return 0
    if current_letter == substring:
        return 1
    
    computed_next_position = sum_tuples(sub_tuples(next_position, current_position), next_position)
    return read(grid, substring[1:], next_position, computed_next_position)
    
count = 0
word = "XMAS"

for line in range(len(grid)):
    for column in range(len(grid[line])):

        current_position = (line, column)

        count += read(grid, word, current_position, (line, column+1)) # left to right
        count += read(grid, word, current_position, (line, column-1)) # right to left
        
        count += read(grid, word, current_position, (line+1, column)) # top to bottom
        count += read(grid, word, current_position, (line-1, column)) # bottom to top

        count += read(grid, word, current_position, (line+1, column+1)) # tl to br
        count += read(grid, word, current_position, (line-1, column-1)) # br to tl

        count += read(grid, word, current_position, (line+1, column-1)) # tr to bl
        count += read(grid, word, current_position, (line-1, column+1)) # bl to tr

print(f"Answer is : '{count}'")

##########################################################################
# STEP 2 OF 2
##########################################################################

count = 0

def read_x(grid, line, column):
    # [line][column]

    tl_br = [grid[line-1][column-1],grid[line+1][column+1]]
    tr_bl = [grid[line-1][column+1],grid[line+1][column-1]]

    if set(tl_br) == set(tr_bl) == set(['M', 'S']):
        return 1

    return 0

for line in range(1,len(grid)-1):
    for column in range(1,len(grid[line])-1):

        current_position = (line, column)
        if grid[line][column] == 'A':

            count += read_x(grid, line, column)

print(f"Answer is : '{count}'")