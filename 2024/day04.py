from collections import Counter
from itertools import product

def part1():

    max_col = len(grid[0])
    max_row = len(grid)
    cols = ['' for _ in range(max_col)]
    rows = ['' for _ in range(max_row)]
    fdiag = ['' for _ in range(max_row + max_col - 1)]
    bdiag = ['' for _ in range(len(fdiag))]
    min_bdiag = -max_row + 1

    for x in range(max_col):
        for y in range(max_row):
            cols[x] += grid[y][x]
            rows[y] += grid[y][x]
            fdiag[x+y] += grid[y][x]
            bdiag[x-y-min_bdiag] += grid[y][x]

    data = (cols+rows+fdiag+bdiag)

    return sum([x.count('XMAS')+x.count('SAMX') for x in data]) 

def part2():
    res = 0
    for x in range(1, len(grid)):
        for y in range(1, len(grid[0])):
            if grid[x][y] == "A":
                try:
                    if Counter(grid[x-1][y-1] + grid[x+1][y-1] + grid[x-1][y+1] + grid[x+1][y+1]) == Counter("MMSS") and grid[x-1][y-1] != grid[x+1][y+1]:
                        res += 1
                except IndexError:
                    pass
    return res

def alt_part2():
    dirs = list(product((-1, +1), repeat=2))  # diagonal (X) directions
    count, I, J = 0, range(1, len(grid)-1), range(1, len(grid[0])-1)

    for i, j in product(I, J):
        if grid[i][j] != 'A':
            continue
        X = [grid[i+i_][j+j_] for i_, j_ in dirs]  # X-neighbors
        if X.count('M') == X.count('S') == 2 and X[1] != X[2]:  # prevent MAMxSAS
            count += 1

    return count

grid = []
with open("day4.txt", "r") as file:
    row = []
    for line in file:
        row = list(line[:-1])
        grid.append(row)

print(part1())
print(part2())
print(alt_part2())