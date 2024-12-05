# -*- coding: utf-8 -*-

symbols = "@#$%&*+-/"

lines = s.split()
lines

ans = 0
nums = []
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        ind = j
        num = 0
        while ind < len(lines[0]) and lines[i][ind].isnumeric():
            num = 10 * num + int(lines[i][ind])
            ind += 1
        if j - 1 >= 0 and lines[i][j - 1] in symbols: #1 char just before the num
            ans += num
            nums.append(num)
        elif ind + 1 < len(lines[0]) and lines[i][ind + 1] in symbols: #1 char just after the num
            ans += num
            nums.append(num)
        elif i - 1 >= 0 and lines[i - 1][j: ind] and all(c in symbols for c in lines[i - 1][j: ind]): # all characters above num
            ans += num
            nums.append(num)
        elif i + 1 < len(lines) and lines[i + 1][j: ind] and all(c in symbols for c in lines[i + 1][j: ind]): #all characters below num
            ans += num
            nums.append(num)
        elif i + 1 < len(lines) and ind + 1 < len(lines[0]) and lines[i + 1][ind + 1] in symbols: #lower right diagonal lines[i + 1][ind + 1]
            ans += num
            nums.append(num)
        elif i + 1 < len(lines) and j - 1 >= 0 and lines[i + 1][j - 1] in symbols: #lower left diagonal lines[i + 1][j - 1]
            ans += num
            nums.append(num)
        elif i - 1 >= 0 and j - 1 >= 0 and lines[i - 1][j - 1] in symbols: #upper left diagonal lines[i - 1][j - 1]
            ans += num
            nums.append(num)
        elif i - 1 >= 0 and ind + 1 < len(lines[0]) and lines[i - 1][ind + 1] in symbols: #upper right diagonal lines[i - 1][ind + 1]
            ans += num
            nums.append(num)


print(ans)
print(nums)

def is_valid_char(char):
    return char.isdigit()

def is_valid_symbol(char):
    return char in '@#$%^&*+-/'

def is_part_number(engine, row, col):
    return is_valid_char(engine[row][col]) and any(is_valid_symbol(engine[i][j]) for i in range(row-1, row+2) for j in range(col-1, col+2) if 0 <= i < len(engine) and 0 <= j < len(engine[0]))

def part_numbers(engine):
    return list((row, col) for row in range(len(engine)) for col in range(len(engine[0])) if is_part_number(engine, row, col))


pairs = part_numbers(lines)

print("pairs of all part numbers:", pairs)

m, n = len(lines), len(lines[0])
result = 0
for r, c in pairs:
    ind, num = c, 0
    while ind < n and lines[r][ind].isdigit():
        num = num * 10 + int(lines[r][ind])
        ind += 1
        if (r, ind) in pairs: pairs.remove((r, ind))

    result += num

print("sum is", result)

ans = 0
nums = []

for i, line in enumerate(lines):
    j = 0
    while j < len(lines[0]):
        ind = j
        num = 0
        while ind < len(lines[0]) and lines[i][ind].isdigit():
            num = 10 * num + int(lines[i][ind])
            ind += 1
        print(num)
        if (j - 1 >= 0 and lines[i][j - 1] in symbols) or \
           (ind + 1 < len(lines[0]) and lines[i][ind + 1] in symbols) or \
           (i - 1 >= 0 and lines[i - 1][j: ind] and all(c in symbols for c in lines[i - 1][j: ind])) or \
           (i + 1 < len(lines) and lines[i + 1][j: ind] and all(c in symbols for c in lines[i + 1][j: ind])) or \
           (i + 1 < len(lines) and ind + 1 < len(lines[0]) and lines[i + 1][ind + 1] in symbols) or \
           (i + 1 < len(lines) and j - 1 >= 0 and lines[i + 1][j - 1] in symbols) or \
           (i - 1 >= 0 and j - 1 >= 0 and lines[i - 1][j - 1] in symbols) or \
           (i - 1 >= 0 and ind + 1 < len(lines[0]) and lines[i - 1][ind + 1] in symbols):
            ans += num
            nums.append(num)
        j += ind + 1

print(ans)
print(nums)
