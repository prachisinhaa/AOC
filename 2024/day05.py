from collections import defaultdict

def part1(nums):
    for i in range(len(nums)):
        for j in range(0, i + 1):
            if nums[j] in after[nums[i]]: 
                return False
    return True

def part2(nums):
    correct = [0] * len(nums)
    numset = set(nums)
    for i in range(len(nums)):
        pos = 0
        for x in after[nums[i]]:
            if x in numset:
                pos += 1
        correct[pos] = nums[i]
    correct.reverse()
    return correct[len(nums) // 2]

p1, p2 = 0, 0
after = defaultdict(set)

with open("day5.txt") as file:
    for line in file:
        if "|" in line: 
            x, y = map(int, line.split("|"))
            after[x].add(y)

        elif line != "\n":
            to_print = list(map(int, line.split(",")))
            if part1(to_print):
                p1 += to_print[len(to_print) // 2]
            else:
                p2 += part2(to_print)
print(p1)
print(p2)