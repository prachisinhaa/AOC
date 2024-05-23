def get_full_number(x, y, schematic, searched):
    # Find first digit and last digit of part number
    y_min, y_max = y, y
    while y_min - 1 >= 0 and schematic[x][y_min - 1].isdigit():
        y_min -= 1
    while y_max < len(schematic[x]) and schematic[x][y_max].isdigit():
        y_max += 1

    # It is needed to filter out doubles as a part number might be visited twice.
    # Hence the need to return a 0 and filter it out later.
    # Yes I know ... could be optimised to stop looking earlier and not use a 0, stop nagging mom(!).
    number = '0'
    if [x, y_min, y_max] not in searched:
        number = ''.join(schematic[x][y_min:y_max])
        searched.append([x, y_min, y_max])

    return int(number)


# Find all adjacent numbers for a part.
def adjacent_numbers(i, j, schematic, searched):
    numbers = []
    for x in range(-1, 1 + 1):
        for y in range(-1, 1 + 1):
            if schematic[i + x][j + y].isdigit():
                number = get_full_number(i + x, j + y, schematic, searched)
                if number != 0:
                    numbers.append(number)

    return numbers


def solve(data, gears=False):
    schematic = [[c for c in line] for line in data]

    # Find all parts by part symbol together with their adjacent numbers.
    searched, parts = [], []
    for i in range(0, len(schematic)):
        for j in range(0, len(schematic[i])):
            if not schematic[i][j].isdigit() and schematic[i][j] != '.':
                parts.append([schematic[i][j], adjacent_numbers(i, j, schematic, searched)])

    if gears:
        # For gears first calcualte the gear ratios (product) and then sum those.
        return sum([numpy.prod(part[1]) for part in parts if part[0] == '*' and len(part[1]) == 2])
    else:
        # Make the sum of all numbers of the parts
        return sum([sum(part[1]) for part in parts])

print(solve(s, True))

import numpy

# Meta data
day = 3
year = 2023
p1_expected_tst_result = 4361
p2_expected_tst_result = 467835

# Download daily input


def get_full_number(x, y, schematic, searched):
    # Find first digit and last digit of part number
    y_min, y_max = y, y
    while y_min - 1 >= 0 and schematic[x][y_min - 1].isdigit():
        y_min -= 1
    while y_max < len(schematic[x]) and schematic[x][y_max].isdigit():
        y_max += 1

    # It is needed to filter out doubles as a part number might be visited twice.
    # Hence the need to return a 0 and filter it out later.
    # Yes I know ... could be optimised to stop looking earlier and not use a 0, stop nagging mom(!).
    number = '0'
    if [x, y_min, y_max] not in searched:
        number = ''.join(schematic[x][y_min:y_max])
        searched.append([x, y_min, y_max])

    return int(number)


# Find all adjacent numbers for a part.
def adjacent_numbers(i, j, schematic, searched):
    numbers = []
    for x in range(-1, 1 + 1):
        for y in range(-1, 1 + 1):
            if schematic[i + x][j + y].isdigit():
                number = get_full_number(i + x, j + y, schematic, searched)
                if number != 0:
                    numbers.append(number)

    return numbers


def solve(data, gears=False):
    schematic = [[c for c in line] for line in data]

    # Find all parts by part symbol together with their adjacent numbers.
    searched, parts = [], []
    for i in range(0, len(schematic)):
        for j in range(0, len(schematic[i])):
            if not schematic[i][j].isdigit() and schematic[i][j] != '.':
                parts.append([schematic[i][j], adjacent_numbers(i, j, schematic, searched)])

    if gears:
        # For gears first calcualte the gear ratios (product) and then sum those.
        return sum([numpy.prod(part[1]) for part in parts if part[0] == '*' and len(part[1]) == 2])
    else:
        # Make the sum of all numbers of the parts
        return sum([sum(part[1]) for part in parts])


p2_tst_result = solve(s, True)
print(f"Test solution: {p2_tst_result}.")

