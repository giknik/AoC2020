#
# AoC 2020 py solution for day 3
#   Part 1 go down the slope R3 D1:
#   How many trees do you encounter
#   from top to bottom.
#

with open('slope.txt') as f:
    lines = f.read().splitlines()

tree = 0
right = 0

for line in lines:
    if right > len(line) - 1:
        right = right - len(line)
    if line[right] == "#":
        tree += 1
    right += 3

print(tree)
