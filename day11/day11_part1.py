#
# AoC 2020 py solution for day 11
#   Part 1 airport launge:
#   find number of seats that are
#   ocupied at the end.
#

with open('seats.txt') as f:
    lines = [list(line) for line in f]

Y = len(lines) - 1
X = len(lines[0]) - 2


def neighbours(y, x):
    return [(x2, y2) for x2 in range(x - 1, x + 2) for y2 in range(y - 1, y + 2) if (-1 < x <= X and -1 < y <= Y and
            (x != x2 or y != y2) and (0 <= x2 <= X) and (0 <= y2 <= Y))]


def count_ocupied(rows):
    ocupied = 0
    for row in rows:
        ocupied += row.count("#")
    return ocupied


def rounds(rows):
    rows2 = [row[:] for row in rows]
    changes = 0
    ct = 0
    n_ocupied = True
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            print(i, j)
            for x, y in neighbours(i, j):
                if rows[y][x] == '#':
                    n_ocupied = False
                    ct += 1
            if rows[i][j] == 'L':
                if n_ocupied:
                    rows2[i][j] = '#'
                    changes += 1
            elif rows[i][j] == '#':
                if ct >= 4:
                    rows2[i][j] = 'L'
                    changes += 1
            ct = 0
            n_ocupied = True
    return rows2, changes


curr_changes = 1
while curr_changes != 0:
    lines, curr_changes = rounds(lines)

print(count_ocupied(lines))
