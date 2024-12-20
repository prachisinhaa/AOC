# -*- coding: utf-8 -*-
"""day16_2023.ipynb
"""

sample = '''.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....'''


txt = s
grid = [list(x) for x in txt.split("\n")]

steps = {("R", "|"): ("U", "D"), ()}

def dfs(x, y, dir):
    m, n = len(grid), len(grid[0])
    if not 0 <= x <
    if grid[x][y] == "|" and dir in "LR":
        dfs(x + 1, y, "D")
        dfs(x - 1, y, "U")

    elif grid[x][y] == "-" and dir in "UD":
        dfs(x, y - 1, "L")
        dfs(x, y + 1, "R")
    elif grid[x][y] == "/" and dir == "L":
        dfs(x + 1, y, "D")
    elif grid[x][y] == "/" and dir == "R":
        dfs(x - 1, y, "U")

import sys

a = grid

D = {'R': (0,1), 'L': (0,-1), 'U': (-1,0), 'D': (1,0)}

def energise(start):
    energized = set()
    visited = set()
    q = [start]

    while q:
        chr = q.pop()  #n, direction
        if chr in visited: continue
        energized.add(chr[0])
        d = chr[1]
        visited.add(chr)

        n = (chr[0][0] + D[d][0], chr[0][1] + D[d][1])
        if n[0] < 0 or n[0] >= len(a) or n[1] < 0 or n[1] >= len(a[n[0]]): continue
        curr = a[n[0]][n[1]]
        if curr == '\\':
            if d in 'RU': d ='LD'[d == 'R']
            elif d in 'LD': d ='RU'[d == 'L']
            q.append((n, d))

        elif curr == '/':
            if d in 'RD': d ='LU'[d == 'R']
            elif d in 'LU': d ='RD'[d == 'L']
            q.append((n, d))

        elif curr =='|' and d in 'RL':
            q.append((n,'U'))
            q.append((n,'D'))

        elif curr =='-' and d in 'UD':
            q.append((n,'R'))
            q.append((n,'L'))

        else: q.append((n, d))

    return len(energized) - 1

m = energise(((0,-1),'R'))
print(m)

for i in range(len(a)):
    m = max(m,energise(((i,-1),'R')))
    m = max(m,energise(((i,len(a[0])),'L')))
for i in range(len(a[0])):
    m = max(m,energise(((-1,i),'D')))
    m = max(m,energise(((len(a),i),'U')))

print(m)
