#
# AoC 2020 py solution for day 12
#   Part 1 evasive actions:
#   make all the moves and
#   calculate the Manhattan distance
#

with open('moves.txt') as f:
    lines = f.read().splitlines()

nesw = [0, 0, 0, 0]
curr_direction = 90

for move in lines:
    direction, val = move[0], int(move[1:])
    if direction in "NESW":
        nesw["NESW".index(direction)] += val
    elif direction in "LR":
        if direction == "L":
            curr_direction = abs((360 + curr_direction - val)) % 360
        else:
            curr_direction = ((curr_direction + val) % 360)
    else:
        nesw[int(curr_direction/90)] += val

print(abs(nesw[0]-nesw[2]) + abs(nesw[1] - nesw[3]))

