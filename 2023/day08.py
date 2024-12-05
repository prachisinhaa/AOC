# -*- coding: utf-8 -*-
"""day8_9.ipynb
"""

slist = s.strip().split("\n")

seq, m = slist[0], slist[2:]

map = {}
for line in m:
    key, val = line.split(" = ")
    val1, val2 = val.replace("(", "").replace(")", "").split(", ")
    map[key] = [val1, val2]
    #if val[0] == 'ZZZ' or val[1] == 'ZZZ': print (key, val)

sample = '''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)'''

cnt, state = 0, 'AAA'
for dir in seq * 1000:
    new_state = map[state][dir == "R"]
    cnt += 1
    if new_state == "ZZZ":
        print(cnt)
        break
    state = new_state

def solvesteps(start):
	pos = start
	idx = 0
	while not pos.endswith('Z'):
		d = seq[idx%len(inst)]
		pos = map[pos][0 if d=='L' else 1]
		idx += 1
	return idx
ret = 1
for start in map:
	if start.endswith('A'):
		ret = math.lcm(ret, solvesteps(start))
print("p2", ret)

ll = [x for x in open("input").read().strip().split('\n\n')]
import math
inst = list(ll[0])
conn = {}
for l in ll[1].split("\n"):
	a = l.split(" ")[0]
	b = l.split("(")[1].split(",")[0]
	c = l.split(" ")[3].split(")")[0]
	conn[a] = (b, c)
pos = 'AAA'
idx = 0
while pos != 'ZZZ':
	d = inst[idx%len(inst)]
	pos = conn[pos][0 if d=='L' else 1]
	idx += 1
print("p1", idx)
def solvesteps(start):
	pos = start
	idx = 0
	while not pos.endswith('Z'):
		d = inst[idx%len(inst)]
		pos = conn[pos][0 if d=='L' else 1]
		idx += 1
	return idx
ret = 1
for start in conn:
	if start.endswith('A'):
		ret = math.lcm(ret, solvesteps(start))
print("p2", ret)


