"""#day 14"""

s = '''O...O..###.#..#O...###.......#....O#.O...O....#.O...O..O..##.O.O#...O........O...#.#.O...O#O.......#
...O#..#O...#....O..###.O.....#......#.OO.O#..#.O..##...#....##...#.O....##O##OOO..#.O..OOOO..#..#.#
...##.OOOOO#.OO....OO#O.###.O..O...OO.......O....O...OO##....#..O.....#O#.O.O.#O..O.##....##.#.OOOO#
O..#O..O.....#.#...#....#O.O..#..O.O..#O#..O....O..O.#.O.#..O.O#...#O#...##O.#O.##.OO...#.#.#OOO....
.#O#O.O.......#O.#.O#.O..##.#.O.....#..#.....O..#..###..OO.#.O.OO#..O.O.........O..O...#.O.#....OO#.
..........#...O.OO....#.O.O##OO#......#OO.#.O...O....O..#OO#..O...#..#.#.....O#O#..OO#...#OOO.O.#O..
#O#OO.O.#.O.O...O.###O.........#O.O.#...O.#..O.O..#..O##.#O.O.OO.....OO.#.#.#..#.O..O#......O..O....
.#....O#O.OO..#..O#..O..O..O.#..O..#.O#....#.O....O.O.....#O#....#.#.#..O...O#OO#.#O.#O.#...OO..OO#O
.O.........#.#O#....O.O#OOO......O..#O#...#.....#.......#...#....#.##.O...O..#O..#O...O.#..O.OO..#..
O...O...O.....O..O...........OO.##..OO.OO#.O.##..O#OO#......O..O#.O#.OO..#####......O....#....O...#.
.....#O.....#....#O......#..OO.O.O.#..O..O....O..#.#..#.......O..O.O....O.OO......OOO#.OOO......O...
..O#.O.O.#O#O...#..........#..O##...O..O#OOO.OO..##O.#OOOO...#..O....#.....O...#....#.#.#...OO.O.#..
#.......#.O....O#.#O..#OOO..O..###O#..#.O...OO.O.......##O#..O#...OO.........OOO.#O...O...#OO#O#...O
#O#...#O.##..O.........O#..O..O..........#.##..OOOO...O..#.OO......O#....##....O.O...O.OO...O..OOO.O
.OO..#.....O#O..O..OOOO.#.#..#.O......#..#..O..O..O.#O..OO....#...O##O.O.O.O.#......O...O..#.#O...#.
..OO.O......O.O.OO.....O.#..#.O..#O.#.O.....#.O..OO.OOO#..#.#OO.#.OO#.....##O....#.#O.....#..#......
.#..O#.#O#.....##.O.#......O#.O.#..#O.#..O#.OO.O.#.O#..O.....#.##..###O..O.OO.##.O.O..#......###...O
#.O.O....O##...#..OO..#...O#O....O....O.OO.........#..OO..#...#...OOO#O.....O.#.OO.OO##.O....#......
O#.O.O..#..#....O.O.......#.#...#...##O..O.O...O.OO#..#O.O..O.......#...#O.#.O.#O##.#.O..#..O....#.#
.O.O..#...O#..O....O..#.#.OO......O.O.O.O##........#.O#.#..#....O..O....O...O##OOO..O.#O..O.......##
......#..........O#..O..O..O#.OOO#O.#........#...O.#..OO..#.#.#..O#...###.#...#.#.O#..#O.#O....O..O.
..#.......O...#..O..O#..........#.......#....#...O........##O....#O..OO.###.O#.#O........OO#.#O..O#O
.....#.O.O........O.#.O.#.O...##.......#..#........#.O..O...###...O.O.O#....OO.#.....#.......O#..O..
#..O.O.O#.....#.OOO##.....O..OOO.OO...#..#O..OO.O...##...#..###......O...##..#....#..OOO.O...#OO.#..
..##...O...#O..O#.O.#...O.O#......OO..O...O.#...O.O.OO...O.O.O.#..#O.O........#.#..##.O.....#.#O...O
..#O...O.O.#.O....O#.....#..O.O................O....O..##O#.#O....O.O......O...#.....O..O#...O..#.O.
..#..O.#......O#.O.O...O#...O#.O#...O..O....#..O...#.#......#......#O....O.O.O..O..O..#....O..O.....
..#...O....OOO.O##..O#.#.......O##.....O........OO.O...OO#.....#......O.#O#OO##O....O#.OO........#..
....O##..#.....##.O##...O.#..O...#O.#...#.#...#O....O.O.....O.OO.##..#O...#O.O#.#..O#...............
O..O.......O#O.......OO....O.OO....#...#O.OO#..##O....#..#.#O#OO##O...O.O...#...OO#.....O..#..OO....
..#..#O....#...O.##...#O#.O..O.O....O.....OO#O.#..#.....O..O.###.OO.O.......O..#.......OO.#.#..O....
#.O..O.O.#O..OOO##OO....O.OO#OO...#OO.#.#O.OO.OO...#..O.....O....O.O.O#.OO..O.#..#.O.O..OOO##..O#OO.
O.#O.#.OO.#...#.##..OO...#.O##..#O.#.#.#.....O.O##..O..#..O.O.....#....O...O......O..O##.###..#O.#OO
#.........#....O...O........OOOO.##.O.O.#......O####O..#..O##.O.#O.#O...#..#.....O...#.#..O#.#...#O.
.......#.#OOO.....O#O..#.#....#.OO.....O..OOOO#...#.............###.........O.OO..#.O#O..O...O..#.O.
O#...O.......O.O..O.#.O.....OO...O...O.O#OO....##.##.#O#..........O.O.......#.....O.....O.O..OOO#..#
#.O#......O.O..#O.O..O....#..#O..#.#O.O...OO...##.#.O.O..#..#O.#.#.O#.......O..O.#...#O.....#.O#...O
..O..O#...##.#..##..#O..O.OO#..#.##O.O..O..#.O..##.O#.O..#.O.#...........O#.O...O.O#.#...#..#..O.O.O
#.#.O...OO....O..O.#O.#.OO..O#..O..O....O.#.#O.##O.....#.O.#...#...#....#....OO.......#.O..O...#..#.
..O.O#O..O.......#.......O#OO..O....O##.....O.#.O..#.#.....#...OOO.......#...OO#......O..........O.O
..##.#..O.O..#....##..O...O..O#.#O....O##....##O.....OO.O..#.O.O#.#.....OO..O........#........O#O###
..#.#...O#..O.......#.OO##...OO#O...#.O....#OOO......O.O.O.#O..#.....##..#O#.OOO...O......OOO#.O.O.O
O...#...O..#O......O.O......#.....#...#..#.O...O.#O##..#.#...#..O#....O.#OO#..O.....#.#..#OOO#...OOO
...##..#O...#...O.##O.O#.........O........OO#O..#.OO.#....O..#...OO..#O.......O..O.O#...#......OO..#
.....O.O....O.O#....#O#......O.............O.OO#.....#OO...........O#.......#......OO#O#.OO..O..O...
O##.....O...#.#.#..O..OOOOO..#.#.O##.O...#..O...O.....O.#.#...###O.O..#.#.O..O#....#.O...O#.O.......
#OO.....O.O.#...#.O#.....OO...##.O...O......O.#O.........#.O....OO.OO.#.O.#O.O......#O.###..#.#.OO#.
.OOO..O.OO#O..O##.......##...##......O..O...#...O...#.O.O.#.#O.#OO...O.O..#.O#...O..#...OO....#OO...
.##.O.OOO..O#.##O...#O#O...#...#.....#.....O...O......#..##O.OOO.O#..O.#..#.#..O........O..#.O#O....
....O..O.............#......O.#O..OO...OO.....O..#..#......OO......O....OO..OOOO.....#.#O..#.#...O.O
.###.....##.#......###....O#....O....O...O....#.#O.O#..#..O..#O...OO..OO.O.....#O.O..#.#.....O...O#.
..O..#O...O.OO.O........O...O.O.....O..#O.O.O...#........O........OO.O..OO#O.#.O..#.#O#...O.#.##.O..
OO..OO.O..#OO..OO#..........#...............#.O#....O...O.#.O.O#..#.#.OO#...O.#O..##........O#.O....
#.O......#....#...O.O...O....OO..O..#...O..O..#..O#........###...#..#.#..OO..O.....#.....#...#...O..
..#O.O..O.....OO...............O....#.....O.....#O.OO.O..O..##O....O..#.#.#O...O#O##O#.#OOOOOO.#..O.
#O#O.....O..#...O#......OO...#..OOO#O..O##.OO..#.#.##.#.OO..O.###.O.#..O...#O#....O....O##O..#O.O.O.
..O.....O#.O#.....OOO.O..O......O.O..#O..O.O.........#.###..#.O.O.O.OO#.O..#...O.#..#.#...O##.#...O.
#..O#..O#..#...#.#......##.....#OO.O#.OO..#.....OO#...O.O..O.......O#.#.........O.#O#O.O..#.O.......
..O.#..#..O.O..##..#.#O.......OOO#.O.#.OO.##...O...........#.O..#...#.O........O..O..#.....O.#.....O
O.....O.....O...O....#..#......OO#....O......O..O#.#...O...##.O####O#..O.OO.O.O.O.##...........O...O
OO#.O..##O.O..O..#.#..#...#...O.O.#..#...#.#...O.#..#O......#####..##.OOOOO......O.O..#OO.O.#..O.O..
O.O..#.O.OO.#.O.#....O.#......O.##..#O...O..##.#...O.#...O.O....#...O.#...O.......###....#....#.....
#..#.........O....#........OO.#..OO..OOO....#.....O....##O.O.O....O.O..O....#O#.###.O...#..O.O....#O
#...O##..O#..O..#.O.......O.....#....#O###O#OO.O.O..O...O..OO...#.#.#..O..O...O..#...#.#....#.#.#.OO
......#..........#...#..O..#O#..O....#.O..O..#.O.#O...O#.......#........O#O....OO.....O..OO...#..#..
O..O...#...#..O##....#.O....O..#...O..###..O...O....OO..O..O.........O..##OO......#O...O.O##...OOO.O
..#......OO.#.......#...O#.#.O#...#...#O...O......#.....O#....OO........O#O.......#O..#OO#.O.O....#.
.O.##....#OO.O...O#....O..O......O..#.....#O..O.#...#.......O....OO#...O....#....#.O...OOOOO.#O.O..O
....#....OO#..#O....O...#.OO#...#O......#.#.OOO..#...O#......#...O..##.OO..O....O.#O...OO.#.#.O..O..
O.O....OO#...#..O...O.#OO.O..O.....#....#.O..O.#..........OO..#.#.#.O...O.O.#.#..#.#......#..O.###..
....#..O.O....OO...O.....#.......#........O..#.OO##O#OOO#O.......#.#.#....#.#.O..#.O##.#..O....##.OO
O.....#.#....#.........O.O....O..O#.....#O.O#O...O#O...O...##........OO.O.........OO..#...OO.O..#...
.O....O....#.#O..O...OOO.......O..O..O..#............O.....#.O...OO....#.O#O.O##.#.O........#...O...
..##.O..OO#..O.O...O....##...O.......#..O...O.#O.O..........O.#.#OOO#..O...O..O.OOO.....O.........O.
OO..#..#.....#....##...#..#..##.O.OO...O#........O..O.....#.......O.O.O..O...O.O.OO..O...#.###.#.O##
O.#O...O......O.......O#.O......O#..O..#...##.O...##......O.O.#O.##.O.O#....O#O#..#..#O#...#........
#OOO.O...O...O.#.#O....#....O..#.#..O.......#OO......O........O#..O..##..#.O...O...##O...........O#O
.O.#.OO..O.....O...##O.#O.#...O#..O.#....#..#OO#.#.OO...#.O#...OO......O.....#O..O...O...OOO#.O..O##
..O...O...#..O..O#..O.OO.#.OO.O...OO.#.....#.O..#..#O..OOO.##O#O....#...#O.O....OO..#.O...OO#O#....O
#O..OO.###.OOOO....O#......O.O.#OO......OO..O.O..O...O...O..#.OO.....##.O.OO...O..#O.###..O..OO.#.O.
...O.O##....O.#..O#.OOO#.........#....#....#.......#.O...O...........O.O#O.O#..OO.O#....O.#.O.#O.O..
#....#....O..O..#.....#..O#O.#..O.O.#O.O....OO.#.#.O.O....#O....#..O..#.O.#O...#.....O.O...#..#...O.
.#....O.....O..OO.O.O#..#...##.....OO....#.#.OO.#..O..O.......#......#.....OOO#O.#######.##......O#O
#OO..#..OOOO.O..#.###..#.O..#.O...O#.O..#....#...#OO#..#....#OO....#...OO..#...O.O.....OO...#.O.#...
#..O....OO....#.#.OO...O.O....O.##..#.O..O....OO..#.O..O.OO......#.#O..O.O........O.O.O...O.....O#.O
.O.#...O.#....O..O#.O..O.OO.....O...........#.##OO....O..#O###..#..O.O.O.....#.......##O#.#...O.....
.....O.OO.#O.O##............O.O...##.O......#....#....#...#.#...O...#OO.#.O.....O.#..O...........#..
..O.OO..#O..O.O.##.O#..........OO..O...OO..OO.OO.OO#...O.#O.O...OO.......#OO.#..#..O...#....O.......
O.OO....O#....#...#.#O##..O#...#..#......O.......#O..#O..O..O...#......#O..O##.O....O..O.O#.#....O..
.#.O..O..O.........##O..#..OOO...O##.O.#O#.O...O.#....#..O..O.......O..#..O..O#..#....O..OO.##..O...
...#...OO.OOO..#...O.#.O.......#...##.O#.##..##..#..#.##.....##O..O..O..#OO...#....O..O.......#..#O.
.....O...O.#......##O.O..#...#.....O..O....#O#.#..#O.#....O#.O...#O....###...OOO...O#..O..O..###..O.
..#..........O..O..O...O...O....O............O.....#O....O..#.....#...O.....#..O.#.#..O..O...O.#O...
...OOO......O...#.O#....##..#...O..O#..##..O....#.O.OO.......#....O....##.#.#.O...O#.#O..OOO..O.O...
O...#.O....O..OO..O...O....#.#.....#O#O....#O.##.O.OO.#.O............#.O#...OO..OO#..#O.#....O......
#.O.....#.O#.OO.#........O..O.#.OO.........#..#...#.O#O...O...O..OO.#.......O.O..#..O.O...OO..O..O.O
..#....#O#.O.O#.OO..O...#..O......O#O.......OO..OO.....#O#.O.O..#O.......OO.#.O..O....O.O.O.........
#...O###O..O.O##..#.#.##..#...#.#.#...O.#....#.....#.#...O#..O.O...O..O........#.###....O...#..#...#
.......O........O.....##..O##...O...OO..#O..O...#...O.........#OO.....OO.O..O..#OO.#.#O..O#.OO...#O.
.OO..O.....#.O.....#O..#O...O....#..O.....#....#O......O...#.O###.OO......O..O.......#####.........O'''

sample = '''
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....'''

mat = [list(x) for x in s.split("\n")]
trans = list(zip(*mat))



def shift(row):
    load = 0
    cnt0 = 0
    n = len(row)

    for i in range(len(row) - 1, -1, -1):
        if row[i] == "O":
            cnt0 += 1
        if row[i] == "#":
            load += sum(range(n - i - cnt0 ,  n - i ))
            cnt0 = 0
        elif i == 0:
            load += sum(range(n - cnt0 + 1, n + 1))
            cnt0 = 0
        #print(load, i)

    return load

result = 0
for row in trans:
    result += shift(row)
result

grid = list(map(list, s.split("\n")))

def slide(grid):
    n, m = len(grid), len(grid[0])
    for j in range(m):
        ci = 0
        for i in range(n):
            if grid[i][j] == "#": ci = i + 1
            if grid[i][j] == "O":
                grid[i][j] = "."
                grid[ci][j] = "O"
                ci += 1

def get_load(grid):
    n = len(grid)
    return sum((n - i) * grid[i].count("O") for i in range(n))

def rotate(grid):
    n, m = len(grid), len(grid[0])
    new_grid = [["." for j in range(n)] for i in range(m)]
    for i in range(n):
        for j in range(m):
            new_grid[j][n - i - 1] = grid[i][j]
    return new_grid

def to_str(grid):
    return "".join(["".join(row) for row in grid])

d = {}
goal = 1000000000
idx = 1
while True:
    for j in range(4):
        slide(grid)
        grid = rotate(grid)
    x = to_str(grid)
    if x in d:
        cyclen = idx - d[x][0]
        for a,b in d.values():
            if a >= d[x][0] and a % cyclen == goal % cyclen:
                print(b)
        break
    d[x] = (idx, get_load(grid))
    idx += 1




