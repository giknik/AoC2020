#
# AoC 2020 py solution for day 2
#   Part 1 find invalid passwords:
#   Find all paswodrds that don't meat
#   their criteria.
#

with open('data.txt') as f:
    lines = f.read().splitlines()

invalid = 0

for line in lines:
    crit, char, passw = line.split(" ")
    low, high = crit.split("-")
    if int(high) >= passw.count(char[0]) >= int(low):
        invalid += 1

print(invalid)
