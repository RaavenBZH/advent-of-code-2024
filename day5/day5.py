##########################################################################
# STEP 1 OF 2
##########################################################################

import os,copy
directory = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory, "input.txt")

order_data = {}
update_data = []
count = 0

# Retrieve data
with open(filepath, 'r') as file:
    for line in file:

        if line.strip() == "":
            continue
    
        if "|" in line:
            numbers = list(map(int,line.strip().split('|')))

            # Add rule y after x
            before,after = numbers[0],numbers[1]
            if before in order_data.keys():
                order_data[before].append(after)
            else:
                order_data[before] = [after]
        
        else:
            numbers = list(map(int,line.strip().split(',')))
            update_data.append(numbers)

# Check data
for update in update_data:
    is_correctly_ordered = True
    
    for index in range(len(update)):
        after = update[index+1:]
        number = update[index]

        for num in after:
            if number in order_data[num]:
                is_correctly_ordered = False
                break

        if not is_correctly_ordered:
            break
    
    if is_correctly_ordered:
        count += update[int(len(update)/2 - .5)]

print(f"Answer is : '{count}'")

##########################################################################
# STEP 2 OF 2
##########################################################################

count = 0

# Check data
for update in update_data:
    is_correctly_ordered = True
    
    for index in range(len(update)):
        after = update[index+1:]
        number = update[index]

        for num in after:
            if number in order_data[num]:
                is_correctly_ordered = False
                update = sorted(update, key=lambda x: len(list(filter(lambda n: n in order_data.get(x, []), update))))
                break

        if not is_correctly_ordered:
            break
    
    if not is_correctly_ordered:
        count += update[int(len(update)/2 - .5)]

print(f"Answer is : '{count}'")