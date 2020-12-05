#
# AoC 2020 py solution for day 3
#   Part 2 go down the slope with diffrent patterns:
#   How many trees do you encounter on each pattern
#   than multiply the results.
#

import math

with open('slope.txt') as f:
    lines = f.read().splitlines()

tree = [0, 0, 0, 0, 0]
right = [0, 0, 0, 0, 0]
down = 0

for line in lines:
    for i in range(len(right)):
        if right[i] > len(line) - 1:
            right[i] = right[i] - len(line)
        if i == 4:
            if down % 2 == 0:
                if line[right[i]] == "#":
                    tree[i] += 1
                right[i] += 1
        else:
            if line[right[i]] == "#":
                tree[i] += 1
            right[i] += i*2 + 1
    down += 1

print(math.prod(tree))
