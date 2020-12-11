#
# AoC 2020 py solution for day 11
#   Part 2 airport launge:
#   find number of seats that are
#   ocupied at the end by new rules.
#

with open('seats.txt') as f:
    lines = [list(line.rstrip()) for line in f]

Y = len(lines) - 1
X = len(lines[0]) - 1


def neighbours(arr, y, x):
    if arr[y][x] == '.':
        return []
    all_n = []

    # check left and up
    helpx = x - 1

    while helpx >= 0:
        if arr[y][helpx] != '.':
            all_n.append((helpx, y))
            break
        helpx -= 1

    helpy = y - 1

    while helpy >= 0:
        if arr[helpy][x] != '.':
            all_n.append((x, helpy))
            break
        helpy -= 1

    # check right and down
    helpx = x + 1

    while helpx <= X:
        if arr[y][helpx] != '.':
            all_n.append((helpx, y))
            break
        helpx += 1

    helpy = y + 1

    while helpy <= Y:
        if arr[helpy][x] != '.':
            all_n.append((x, helpy))
            break
        helpy += 1

    # check diagonal 1
    helpx = x + 1
    helpy = y + 1

    while helpx <= X and helpy <= Y:
        if arr[helpy][helpx] != '.':
            all_n.append((helpx, helpy))
            break
        helpx += 1
        helpy += 1

    helpx = x - 1
    helpy = y - 1

    while helpx >= 0 and helpy >= 0:
        if arr[helpy][helpx] != '.':
            all_n.append((helpx, helpy))
            break
        helpx -= 1
        helpy -= 1

    # check diagonal 2
    helpx = x + 1
    helpy = y - 1

    while helpx <= X and helpy >= 0:
        if arr[helpy][helpx] != '.':
            all_n.append((helpx, helpy))
            break
        helpx += 1
        helpy -= 1

    helpx = x - 1
    helpy = y + 1

    while helpx >= 0 and helpy <= Y:
        if arr[helpy][helpx] != '.':
            all_n.append((helpx, helpy))
            break
        helpx -= 1
        helpy += 1

    return all_n


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
            for x, y in neighbours(rows, i, j):
                if rows[y][x] == '#':
                    n_ocupied = False
                    ct += 1
            if rows[i][j] == 'L':
                if n_ocupied:
                    rows2[i][j] = '#'
                    changes += 1
            elif rows[i][j] == '#':
                if ct >= 5:
                    rows2[i][j] = 'L'
                    changes += 1
            ct = 0
            n_ocupied = True
    return rows2, changes


curr_changes = 1
while curr_changes != 0:
    lines, curr_changes = rounds(lines)

print(count_ocupied(lines))
