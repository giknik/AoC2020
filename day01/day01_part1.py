#
# AoC 2020 py solution for day 1
#   Part 1 check the expense report:
#   find two items that combine for 2020
#   and print their multiple,
#

with open('report.txt') as f:
    lines = f.read().splitlines()


def expense_report(li):
    for i in li:
        for j in li:
            if i != j and i + j == 2020:
                print(i*j)
                return


expense_report([x for x in map(int, lines)])
