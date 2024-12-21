##########################################################################
# STEP 1 OF 2
##########################################################################

import os 
directory = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory, "input.txt")
file = open(filepath, "r")
lines1 = []
lines2 = []

for line in file:
    line_tmp = list(map(int,line.split("   ")))
    lines1.append(line_tmp[0])
    lines2.append(line_tmp[1])
file.close()

lines1.sort()
lines2.sort()

sum_of_differences = 0
for i in range(len(lines1)):
    sum_of_differences += abs(lines1[i] - lines2[i])

print(f"Answer is : '{sum_of_differences}'")

##########################################################################
# STEP 2 OF 2
##########################################################################

sum_of_products = 0
for number in lines1:
    sum_of_products += number * lines2.count(number)

print(f"Answer is : '{sum_of_products}'")