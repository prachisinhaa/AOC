def part1(target, nums, cur, i):
    if i == len(nums):
        return cur == target
    return part1(target, nums, cur + nums[i], i + 1) or part1(target, nums, cur * nums[i], i + 1)

def part2(target, nums, cur, i):
    if i == len(nums):
        return cur == target
    return part2(target, nums, cur + nums[i], i + 1) or part2(target, nums, cur * nums[i], i + 1) or part2(target, nums, int(str(cur) + str(nums[i])), i + 1)

p1, p2 = 0, 0

grid = open('day7.txt').read().strip().split("\n")

for line in grid:
    target, rest = line.split(": ")
    target = int(target)
    rest = list(map(int, rest.split()))

    if part1(target, rest, rest[0], 1):
        p1 += target

    if part2(target, rest, rest[0], 1):
        p2 += target

print(p1)
print(p2)