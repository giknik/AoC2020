#
# AoC 2020 py solution for day 2
#   Part 2 find invalid passwords:
#   Find all paswodrds that don't meat
#   their actual criteria.
#

with open('data.txt') as f:
    lines = f.read().splitlines()

valid = 0

for line in lines:
    crit, char, passw = line.split(" ")
    low, high = map(int, crit.split("-"))
    if not ((passw[low-1] == char[0] and passw[high-1] == char[0]) or
            (passw[low-1] != char[0] and passw[high-1] != char[0])):
        valid += 1

print(valid)
