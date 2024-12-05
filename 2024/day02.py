def part1(nums):
    pos = nums[1] > nums[0]
    for x, y in zip(nums, nums[1:]):
        if pos:
            if not 1 <= y - x <= 3:
                return False
        else:
            if not 1 <= x - y <= 3:
                return False
    return True

def part2(nums):
    pos = nums[1] > nums[0]
    unsafe = 0

    for x, y in zip(nums, nums[1:]):
        if (pos and not 1 <= y - x <= 3) or (not pos and not 1 <= x - y <= 3):
                unsafe += 1

    return unsafe <= 1

def alternate_part2(nums):
    unsafe = 0
    if nums[0] > nums[1]: nums.reverse()
    for x, y in zip(nums, nums[1:]):
        if not 1 <= y - x <= 3:
            unsafe += 1
    return unsafe <= 1

p1, p2 = 0, 0
with open("day2.txt", "r") as file:
    for line in file:
        nums = list(map(int, line.split()))
        p1 += part1(nums)
        p2 += part2(nums)
        
print(p1)
print(p2)