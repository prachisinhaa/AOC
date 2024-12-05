

def part1(line, x):
    res, i = "", x
    while i < len(line) and line[i].isdigit():
        res += line[i]
        i += 1

    if i < len(line) and line[i] != ",": 
        return 0

    i += 1

    ans = ""
    while i < len(line) and line[i].isdigit():
        ans += line[i]
        i += 1

    if i < len(line) and line[i] != ")": 
        return 0

    try:
        return int(res) * int(ans)
    except:
        return 0

import re


p1, p2 = 0, 0
do = True

with open("day3.txt", "r") as file:
    for line in file:
        for i in range(len(line)-2):
            if not do and line[i:i+4] == "do()": 
                do = True
            if do and line[i:i+7] == "don't()": 
                do = False

            res = part1(line, i+4)
            if line[i:i+4] == "mul(":
                p1 += res
            if do:
                p2 += res
print(p1)
print(p2)

# 7002/3390

'''
---------------- ALTERNATE SOLUTION ----------------
-------------------- Using regex -------------------
with open("day3.txt") as file:
    b = file.read()

pattern = r"mul\((\d+),(\d+)\)"
matches = re.findall(pattern, b)
total_sum = 0
for match in matches:
    num1, num2 = map(int, match)
    print(num1,num2)
    total_sum += (num1 * num2)


print(total_sum)
'''