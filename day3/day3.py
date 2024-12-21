##########################################################################
# STEP 1 OF 2
##########################################################################

import os,re
directory = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(directory, "input.txt")

regex = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
count = 0

def literal_mul_function_to_int(literal : str):
    regex = "[0-9]{1,3}"
    numbers = re.findall(regex, literal)
    numbers = list(map(int, numbers))
    return numbers[0] * numbers[1]

with open(filepath, "r") as file:
    for line in file:
        mul_array = re.findall(regex, line)
        products_array = [literal_mul_function_to_int(mul) for mul in mul_array]
        count += sum(products_array)

print(f"Answer is : '{count}'")

##########################################################################
# STEP 2 OF 2
##########################################################################

count = 0

is_enabled = True

with open(filepath, "r") as file:
    for line in file:

        mul_array = []
        last_index = 0

        pattern = re.compile(r"(don't\(\)|do\(\))")
        matches = list(pattern.finditer(line))

        for match in matches:
            instruction = match.group()
            start, end = match.span()

            if is_enabled:
                mul_array += re.findall(regex, line[last_index:start])

            if instruction == "don't()":
                is_enabled = False
            elif instruction == "do()":
                is_enabled = True

            last_index = end

        if is_enabled:
            mul_array += re.findall(regex, line[last_index:])

        products_array = [literal_mul_function_to_int(mul) for mul in mul_array]
        count += sum(products_array)

print(f"Answer is : '{count}'")