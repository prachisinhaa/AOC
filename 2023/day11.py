
"""#day 11"""


import numpy as np
import itertools

def day11(s, *, part2 = True):
  grid = np.array([list(line) for line in s.splitlines()])
  galaxies = np.argwhere(grid == '#')
  growth = 999_999 if part2 else 1
  emptys = []
  for _ in range(2):
    emptys.append({i for i in range(grid.shape[0]) if np.all(grid[i] == '.')})
    grid = grid.T

    print(galaxies)

  total = 0
  for g1, g2 in itertools.combinations(galaxies, 2):
    for a, b, empty in zip(g1, g2, emptys):
      total += abs(a - b) + growth * len(set(range(min(a, b) + 1, max(a, b))) & empty)

  return total

day11(s)

