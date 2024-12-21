##########################################################################
# STEP 1 OF 2
##########################################################################

import os,copy
directory = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory, "input.txt")

count = 0

with open(filepath, "r") as file:
    for line in file:
        numbers = list(map(int, line.split()))

        is_increasing = all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))
        is_decreasing = all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))
        gaps_short_enough = all(abs(numbers[i] - numbers[i + 1]) < 4 for i in range(len(numbers) - 1))

        if (is_increasing or is_decreasing) and gaps_short_enough:
            count += 1

print(f"Answer is : '{count}'")

##########################################################################
# STEP 2 OF 2
##########################################################################

count = 0

with open(filepath, "r") as file:
    for line in file:
        numbers = list(map(int, line.split()))

        is_increasing = all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))
        is_decreasing = all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))
        gaps_short_enough = all(abs(numbers[i] - numbers[i + 1]) < 4 for i in range(len(numbers) - 1))

        if not ((is_increasing or is_decreasing) and gaps_short_enough):
            for i in range(len(numbers)):
                clone = copy.deepcopy(numbers)
                clone.pop(i)

                is_increasing = all(clone[i] < clone[i + 1] for i in range(len(clone) - 1))
                is_decreasing = all(clone[i] > clone[i + 1] for i in range(len(clone) - 1))
                gaps_short_enough = all(abs(clone[i] - clone[i + 1]) < 4 for i in range(len(clone) - 1))

                if (is_increasing or is_decreasing) and gaps_short_enough:
                    count += 1
                    break
        else:
            count += 1

print(f"Answer is : '{count}'")