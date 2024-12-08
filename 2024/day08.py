from collections import defaultdict

grid = open('day8.txt').read().strip().split("\n")
char_pos = defaultdict(list)
for i, line in enumerate(grid):
    for j, ch in enumerate(line):
        if ch.isalpha() or ch.isdigit():
            char_pos[ch].append((i, j))

def part1():
    seen = set()
    for ch in char_pos:
        for i in range(len(char_pos[ch])):
            for j in range(i + 1, len(char_pos[ch])):
                a, b, c, d = char_pos[ch][i][0], char_pos[ch][i][1], char_pos[ch][j][0], char_pos[ch][j][1],
                diffx, diffy = abs(a - c), abs(b - d)
                if a < c:
                    ax, bx = a - diffx, c + diffx
                    if b < d:
                        ay, by = b - diffy, d + diffy
                    else:
                        ay, by = b + diffy, d - diffy
                else:
                    ax, bx = a + diffx, c - diffx
                    if b < d:
                        ay, by = b - diffy, d + diffy
                    else:
                        ay, by = b + diffy, d - diffy
                if (ax not in range(len(grid)) or ay not in range(len(grid[0]))) and  (bx not in range(len(grid)) or by not in range(len(grid[0]))):
                    continue
                if ax in range(len(grid)) and ay in range(len(grid[0])): seen.add((ax, ay))
                if bx in range(len(grid)) and by in range(len(grid[0])): seen.add((bx, by))
    return len(seen)

def part2():
    seen = set()
    for ch in char_pos:
        for i in range(len(char_pos[ch])):
            for j in range(i + 1, len(char_pos[ch])):
                a, b, c, d = char_pos[ch][i][0], char_pos[ch][i][1], char_pos[ch][j][0], char_pos[ch][j][1]
                seen.add((a, b))
                seen.add((c, d))
                diffx, diffy = abs(a - c), abs(b - d)
                for multiplier in range(1, 60): 
                    curr_diffx, curr_diffy = multiplier * diffx, multiplier * diffy

                    if a < c:
                        ax, bx = a - curr_diffx, c + curr_diffx
                        if b < d:
                            ay, by = b - curr_diffy, d + curr_diffy
                        else:
                            ay, by = b + curr_diffy, d - curr_diffy
                    else:
                        ax, bx = a + curr_diffx, c - curr_diffx
                        if b < d:
                            ay, by = b - curr_diffy, d + curr_diffy
                        else:
                            ay, by = b + curr_diffy, d - curr_diffy

                    if (ax not in range(len(grid)) or ay not in range(len(grid[0]))) and  (bx not in range(len(grid)) or by not in range(len(grid[0]))):
                        continue
                    if ax in range(len(grid)) and ay in range(len(grid[0])): seen.add((ax, ay))
                    if bx in range(len(grid)) and by in range(len(grid[0])): seen.add((bx, by))
    return len(seen)

p1 = part1()
p2 = part2()

print(p1)
print(p2)