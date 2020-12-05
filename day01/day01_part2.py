#
# AoC 2020 py solution for day 1
#   Part 2 check the expense report again:
#   find three items that combine for 2020
#   and print their multiple,
#

with open('report.txt') as f:
    lines = f.read().splitlines()


def expense_report2(li):
    for i in li:
        for j in li:
            for k in li:
                if i != j and j != k and i + j + k == 2020:
                    print(i*j*k)
                    return


expense_report2([x for x in map(int, lines)])
