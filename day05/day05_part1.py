#
# AoC 2020 py solution for day 5
#   Part 1 find highest pass ID:
#   Binary search for the seat
#   and check ID.
#

import math

with open('passes.txt') as f:
    lines = f.read().splitlines()


def binary(start, end, code, i):
    if i == len(code) - 1:
        return start if code[i] == "F" or code[i] == "L" else end
    if code[i] == "F" or code[i] == "L":
        return binary(start, end - math.ceil((end - start)/2), code, i+1)
    if code[i] == "B" or code[i] == "R":
        return binary(start + math.ceil((end - start)/2), end, code, i+1)


highest_id = 0

for line in lines:
    row, seat = line[0:7], line[7:10]
    r_num = binary(0, 127, row, 0)
    s_num = binary(0, 7, seat, 0)
    if r_num * 8 + s_num > highest_id:
        highest_id = r_num * 8 + s_num

print(highest_id)
