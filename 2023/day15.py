# -*- coding: utf-8 -*-
"""
#day 15
"""


sample = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

lines = s.split(",")
lines

def find_hash(line):
    curr = 0
    for ch in line:
        hash = ord(ch)
        curr += hash
        curr *= 17
        curr = curr % 256
    return curr

res = 0
for line in lines:
    res += find_hash(line)
res

p2 = 0
lenses = [[] for i in range(256)]
lenslengths = [{} for i in range(256)]

for i, l in enumerate(lines):
	label = l.split("=")[0].split("-")[0]
	h = find_hash(label)
	if "-" in l:
		if label in lenses[h]:
			lenses[h].remove(label)
	if "=" in l:
		if label not in lenses[h]:
			lenses[h].append(label)
		lenslengths[h][label] = int(l.split("=")[1])

for box, lns in enumerate(lenses):
	for i, lens in enumerate(lns):
		p2 += (box + 1) * (i + 1) * lenslengths[box][lens]

print( p2)







