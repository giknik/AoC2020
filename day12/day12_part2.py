#
# AoC 2020 py solution for day 12
#   Part 2 evasive actions:
#   find the Manhattan distance
#   with the new rules.
#


def shift(arr, n):
    n = n % len(arr)
    return arr[n:] + arr[:n]


with open('moves.txt') as f:
    lines = f.read().splitlines()

nesw = [0, 0, 0, 0]
waypoint = [1, 10, 0, 0]

for move in lines:
    direction, val = move[0], int(move[1:])
    if direction in "NESW":
        waypoint["NESW".index(direction)] += val
    elif direction in "LR":
        if direction == "L":
            rotate = int(val/90)
        else:
            rotate = int(-val/90)
        waypoint = shift(waypoint, rotate)
    else:
        for i in range(len(nesw)):
            nesw[i] += waypoint[i] * val

print(abs(nesw[0]-nesw[2]) + abs(nesw[1] - nesw[3]))