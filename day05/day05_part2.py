#
# AoC 2020 py solution for day 5
#   Part 2 find your seat ID:
#   Flight is full if you add 1 and take 1
#   from your seat ID those seats also exsist.
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


def qsort(arr):
    if not arr:
        return []
    else:
        pivot = arr[0]
        lesser = qsort([e for e in arr[1:] if e < pivot])
        greater = qsort([e for e in arr[1:] if e >= pivot])
        return lesser + [pivot] + greater


all_passes = []

for line in lines:
    row, seat = line[0:7], line[7:10]
    r_num = binary(0, 127, row, 0)
    s_num = binary(0, 7, seat, 0)
    all_passes.append(r_num * 8 + s_num)


all_passes = qsort(all_passes)
prev = 0
for x in all_passes:
    if x - prev == 2:
        print(x - 1)
        break
    else:
        prev = x
