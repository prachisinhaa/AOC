grid = open('day6.txt').read().strip()

g = [list(r) for r in grid.split("\n")]
n, m = len(g), len(g[0])

for x in range(n):
    for y in range(m):
        if g[x][y] == "^":
            start = x, y

dirs = [(-1,0), (0,1), (1,0), (0,-1)]

#------------ PART 1 ------------
x, y = start
cd = 0
seen = set()
while x in range(n) and y in range(m):
    seen.add((x, y))
    while True:
        cdir = dirs[cd]
        nx, ny = x + cdir[0], y + cdir[1]
        if nx in range(n) and ny in range(m) and g[nx][ny] == "#":
            cd = (cd + 1) % 4
        else:
            x, y = nx, ny
            break
print(len(seen))

#------------ PART 2 ------------
ans = 0
for ox, oy in seen:
    if g[ox][oy] == "#" or g[ox][oy] == "^":
        continue

    g[ox][oy] = "#"

    seen2 = set()
    cd = 0
    cx, cy = start
    while cx in range(n) and cy in range(m) and (cx, cy, cd) not in seen2:
        seen2.add((cx, cy, cd))
        while True:
            cdir = dirs[cd]
            nx, ny = cx + cdir[0], cy + cdir[1]
            if nx in range(n) and ny in range(m) and g[nx][ny] == "#":
                cd = (cd + 1) % 4
            else:
                cx, cy = nx, ny
                break

    if (cx, cy, cd) in seen2:
        ans += 1

    g[ox][oy] = "."

print(ans)