from collections import Counter

arr1, arr2 = [], []
with open('2024d1.txt', 'r') as file:
    for line in file:
        x, y = line.split()
        arr1.append(int(x))
        arr2.append(int(y))

def part1():
    arr1.sort()
    arr2.sort()
    tot = 0

    for x, y in zip(arr1, arr2):
        tot += abs(x - y)
    return tot

def part2():
    tot = 0
    freq = Counter(arr2)

    for x in arr1:
        try:
            tot += x * freq[x]
        except KeyError:
            print("not in dict")
    return tot

print(part1())
print(part2())

# 2024/day06.py