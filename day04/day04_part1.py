#
# AoC 2020 py solution for day 4
#   Part 1 count does missing CID as valid:
#   Check if a passport contains all necessary
#   data but overlook cid.
#

with open('passports.txt') as f:
    lines = f.read().splitlines()

necessary = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def check_passport(arr):
    ct = 0
    for x in arr:
        if x in necessary:
            ct += 1
    return 1 if ct >= 7 else 0


valid = 0
fields = []

for line in lines:
    if line == '':
        valid += check_passport(fields)
        fields = []
    else:
        li = line.split(" ")
        for f in li:
            a, b = f.split(":")
            fields.append(a)

valid += check_passport(fields)

print(valid)
