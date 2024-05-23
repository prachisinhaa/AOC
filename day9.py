"""#day 9

"""

def main():
    sequences = []
    with open('aoc9.txt') as f:
        for line in f:
            sequences.append([int(x) for x in line.strip().split(' ')])

    sum_firsts = 0
    sum_lasts = 0
    for seq in sequences:
        first_last = extrapolate(seq)
        sum_firsts += first_last[0]
        sum_lasts  += first_last[1]

    print('part 1:', sum_lasts)
    print('part 2:', sum_firsts)


def extrapolate(seq: [int]) -> [int, int]:
    if seq[0] == 0 and sum(seq) == 0:
        return [0, 0]

    diffs = []
    for i in range(len(seq)-1):
        diffs.append(seq[i+1] - seq[i])
    return [seq[0] - extrapolate(diffs)[0], seq[-1] + extrapolate(diffs)[1]]


if __name__ == "__main__":
    main()

