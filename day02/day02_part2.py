#
# AoC 2020 py solution for day 2
#   Part 2 find invalid passwords:
#   Find all paswodrds that don't meat
#   their actual criteria.
#

with open('data.txt') as f:
    lines = f.read().splitlines()

invalid = 0
valid = 0

for line in lines:
    crit, char, passw = line.split(" ")
    low, high = crit.split("-")
    if (passw[int(low)-1] == char[0] and passw[int(high)-1] == char[0]) or \
            (passw[int(low)-1] != char[0] and passw[int(high)-1] != char[0]):
        invalid += 1
    else:
        valid += 1

print(valid)
