"""#day 10"""

maze = s.split()

row = len(maze)
col = len(maze[0])

ax = -1
ay = -1
for i in range(row):
    for j in range(col):
        if "S" in maze[i]:
            ax = i
            ay = maze[i].find("S")

with open("aoc10.txt" ,"r") as f:
    R = f.read()
maze = R.split("\n")

row = len(maze)
col = len(maze[0])

O = [[0] * col for _ in range(row)] # part 2

ax = -1
ay = -1
for i in range(row):
    for j in range(col):
        if "S" in maze[i]:
            ax = i
            ay = maze[i].find("S")

dirs = [(0,1),(1,0),(0,-1),(-1,0)]
happy = ["-7J", "|LJ", "-FL", "|F7"]
Sdirs = []
for i in range(4):
    pos = dirs[i]
    bx, by = ax + pos[0], ay + pos[1]
    if 0 <= bx <= row and 0 <= by <= col and maze[bx][by] in happy[i]: Sdirs.append(i)
print(Sdirs)

Svalid = 3 in Sdirs # part 2

# right down left up
transform = {
    (0,"-"): 0,
    (0,"7"): 1,
    (0,"J"): 3,
    (2,"-"): 2,
    (2,"F"): 1,
    (2,"L"): 3,
    (1,"|"): 1,
    (1,"L"): 0,
    (1,"J"): 2,
    (3,"|"): 3,
    (3,"F"): 0,
    (3,"7"): 2,
}

curdir = Sdirs[0]
cx = ax + dirs[curdir][0]
cy = ay + dirs[curdir][1]
ln = 1
O[ax][ay] = 1 # Part 2
while (cx,cy) != (ax,ay):
    O[cx][cy] = 1 # Part 2
    ln += 1
    curdir = transform[(curdir,maze[cx][cy])]
    cx = cx + dirs[curdir][0]
    cy = cy + dirs[curdir][1]
print(ln)
print(ln // 2)

# End Part 1
# Begin Part 2

ct = 0
for i in range(row):
    inn = False
    for j in range(col):
        if O[i][j]:
            if maze[i][j] in "|JL" or (maze[i][j]=="S" and Svalid): inn = not inn
        else:
            ct += inn
print(ct)
