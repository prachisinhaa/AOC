# -*- coding: utf-8 -*-
"""Day6.py
"""

s = '''Time:        35     69     68     87
Distance:   213   1168   1086   1248'''

times, distance = [35, 69, 68, 87], [213, 1168, 1086, 1248]
result = 1
for i, time in enumerate(times):
    record_break = 0
    for t in range(time + 1):
        d = t * (time - t)
        if d > distance[i]:
            record_break += 1
            #print(t, d, distance[i])
    result *= record_break
result

time, dist = 35696887, 213116810861248

result = 1
for t in range(time + 1):
    d = t * (time - t)
    if d > dist:
        result += 1
        #print(t, d)
result

times, distances = [35, 69, 68, 87], [213, 1168, 1086, 1248]

# For bisection, just return True/False
def good_hold_time(time, distance, hold_time):
    time_left = time - hold_time

    if time_left * hold_time > distance:
        return True

    return False

# TODO: find_min_hold_time and find_max_hold_time
# are very similar. Could be broken out to a single
# bisection function.
def find_min_hold_time(time, distance):
    min_hold_time = 1
    max_hold_time = time - 1

    # Use bisect to find the minimum value of hold_time
    while min_hold_time < max_hold_time:
        mid_hold_time = (min_hold_time + max_hold_time) // 2
        if good_hold_time(time, distance, mid_hold_time):
            max_hold_time = mid_hold_time
        else:
            min_hold_time = mid_hold_time + 1

    return min_hold_time

def find_max_hold_time(time, distance):
    min_hold_time = 1
    max_hold_time = time - 1

    # Use bisect to find the minimum value of hold_time
    while min_hold_time < max_hold_time:
        mid_hold_time = (min_hold_time + max_hold_time + 1) // 2
        if good_hold_time(time, distance, mid_hold_time):
            min_hold_time = mid_hold_time
        else:
            max_hold_time = mid_hold_time - 1

    return max_hold_time

# Use bisection to find min/max hold_times
def sim_race(time, distance):

    min_hold_time = find_min_hold_time(time, distance)
    max_hold_time = find_max_hold_time(time, distance)

    return max_hold_time + 1 - min_hold_time

prod = 1
for i in range(len(times)):
    prod *= sim_race(times[i], distances[i])

print('Part 1:', prod)

# Part 2, concatenate all numbers on line
time = 35696887
distance = 213116810861248

print('Part 2:', sim_race(time, distance))

