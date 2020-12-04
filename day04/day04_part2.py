#
# AoC 2020 py solution for day 4
#   Part 2 count does missing CID as valid:
#   Check if a passport contains all necessary
#   data but overlook cid and check if data is valid also.
#

import re

with open('passports.txt') as f:
    lines = f.read().splitlines()

necessary = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def check_data(name, value):
    if name == "byr":
        return 1 if 1920 <= int(value) <= 2002 else 0
    if name == "iyr":
        return 1 if 2010 <= int(value) <= 2020 else 0
    if name == "eyr":
        return 1 if 2020 <= int(value) <= 2030 else 0
    if name == "hgt":
        size = re.split("cm", value)
        if len(size) == 2:
            return 1 if 150 <= int(size[0]) <= 193 else 0
        else:
            size = re.split("in", value)
            if len(size) == 2:
                return 1 if 59 <= int(size[0]) <= 76 else 0
            return 0
    if name == "hcl":
        return 1 if re.search("^#[0-9a-f]{6}$", value) else 0
    if name == "ecl":
        return 1 if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] else 0
    if name == "pid":
        return 1 if len(value) == 9 else 0


def check_passport(arr):
    ct = 0
    for fi, da in arr:
        if fi in necessary:
            ct += check_data(fi, da)
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
            fields.append((a, b))

valid += check_passport(fields)

print(valid)
