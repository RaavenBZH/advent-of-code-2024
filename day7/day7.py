##########################################################################
# STEP 1 OF 2
##########################################################################

from itertools import product
import os

directory = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory, "input.txt")

count = 0

def sort_numbers_out(expression):
    parts = expression.strip().split(':')
    parts[1] = list(map(int,parts[1].strip().split(' ')))
    return parts

def compute(parts):
    expected = int(parts[0])
    combination_length = len(parts[1]) - 1

    for combination in product(['*','+'], repeat=combination_length):
        result = parts[1][0]
        for i in range(combination_length):
            operator = combination[i]
            if operator == '*':
                result = result * parts[1][i+1]
            else:
                result = result + parts[1][i+1]
        if result == expected:
            return expected
    return 0

with open(filepath, 'r') as file:
    for line in file:
        parts = sort_numbers_out(line)
        count += compute(parts)

print(f"Answer is : '{count}'")

##########################################################################
# STEP 2 OF 2
##########################################################################

count = 0

def compute(parts):
    expected = int(parts[0])
    combination_length = len(parts[1]) - 1

    for combination in product(['*','+','||'], repeat=combination_length):
        result = parts[1][0]
        for i in range(combination_length):
            operator = combination[i]
            if operator == '*':
                result = result * parts[1][i+1]
            elif operator == '+':
                result = result + parts[1][i+1]
            else:
                result = int(str(result) + str(parts[1][i+1]))
        if result == expected:
            return expected
    return 0

with open(filepath, 'r') as file:
    for line in file:
        parts = sort_numbers_out(line)
        count += compute(parts)

print(f"Answer is : '{count}'")