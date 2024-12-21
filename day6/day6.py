##########################################################################
# STEP 1 OF 2
##########################################################################

import os,copy,time
directory = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory, "input.txt")

to_right = (0, 1)
to_left = (0, -1)
to_bottom = (1, 0)
to_top = (-1, 0)
directions = [to_top, to_right, to_bottom, to_left]

with open(filepath, 'r') as file:
    original_grid = [list(line.strip()) for line in file]
    for i in range(len(original_grid)):
        if "^" in original_grid[i]:
            start_line = i
            start_column = original_grid[i].index("^")

start_position = (start_line, start_column)

line, column = start_position
current_movement = to_top
path = copy.deepcopy(original_grid)
count = 0

while True:
    if path[line][column] == ".":
        path[line][column] = "X"
        count += 1

    next_line = line + current_movement[0]
    next_column = column + current_movement[1]

    if not (0 <= next_line < len(path) and 0 <= next_column < len(path[0])):
        break

    if path[next_line][next_column] != "#":
        line, column = next_line, next_column
    else:
        current_movement = directions[(directions.index(current_movement) + 1) % 4]

# Ajouter la position de départ
count += 1

print(f"Answer is : '{count}'")

##########################################################################
# STEP 2 OF 2
##########################################################################

# Fonction pour simuler le trajet avec un obstacle ajouté
def simulate_with_obstacle(grid):
    line, column = start_position
    current_movement = to_top
    visited = set()

    while True:
        if (line, column, current_movement) in visited:
            return True
        visited.add((line, column, current_movement))

        next_line = line + current_movement[0]
        next_column = column + current_movement[1]

        if not (0 <= next_line < len(grid) and 0 <= next_column < len(grid[0])):
            break

        if grid[next_line][next_column] != "#":
            line, column = next_line, next_column
        else:
            current_movement = directions[(directions.index(current_movement) + 1) % 4]

    return False

positions = []
for i in range(len(path)):
    for j in range(len(path[0])):
        if path[i][j] == "X" and (i, j) != start_position:
            positions.append((i, j))

valid_positions = 0

for obstacle in positions:
    grid_with_obstacle = copy.deepcopy(original_grid)
    grid_with_obstacle[obstacle[0]][obstacle[1]] = "#"
    if simulate_with_obstacle(grid_with_obstacle):
        valid_positions += 1

print(f"Answer is : '{valid_positions}'")