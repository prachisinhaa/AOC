"""#day 12"""



import collections
import functools

def perm(memo, springs, nos, pos, curr_count, countpos):
    key = (pos, curr_count, countpos)

    if key in memo: return memo[key]

    if pos == len(springs): ret = 1 if len(nos) == countpos else 0

    elif line[pos] == '#':
        ret = perm(memo, line, nos, pos + 1, curr_count + 1, countpos)

    elif line[pos] == '.' or countpos == len(nos):
        if countpos < len(nos) and curr_count == nos[countpos]:
                  ret = perm(memo, line, nos, pos + 1, 0, countpos + 1)
        elif curr_count == 0:
                  ret = perm(memo, line, nos, pos + 1, 0, countpos)
        else: ret = 0

    else:
        hash_count = perm(memo, line, nos, pos + 1, curr_count + 1, countpos)

        dot_count = 0
        if curr_count == nos[countpos]: dot_count = perm(memo, line, nos, pos + 1, 0, countpos + 1)
        elif curr_count == 0: dot_count = perm(memo, line, nos, pos + 1, 0, countpos)

        ret = hash_count + dot_count

    memo[key] = ret
    return ret



@lru_cache(None)
def is_valid(springs, nos):
    current, seen = 0, []
    for c in springs:
        if c == ".":
            if current > 0: seen.append(current)
            current = 0
        elif c == "#":
            current += 1
        else: assert False
    if current > 0: seen.append(current)
    return seen == nos

@lru_cache(None)
def f(springs, nos, i):
    if i == len(springs): return 1 if is_valid(springs, nos) else 0
    if springs[i] == "?": return f(springs[:i] + "#" + springs[i + 1:], nos, i + 1) + f(springs[:i] + "." + springs[i + 1:], nos, i + 1)
    else: return f(springs, nos, i + 1)


result = 0
for line in s.split("\n"):
    springs, nos = line.split(" ")
    nos = list(map(int, nos.split(",")))
    #result += perm({}, springs + ".", nos, 0, 0, 0)
    result += f(springs, nos, 0)
result

