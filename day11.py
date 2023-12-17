import re
from itertools import pairwise

import math

MAX_LEN = 0

universe = []


def day11a():
    global universe
    with open("day11.txt") as myfile:
        universe = myfile.read().split('\n')

    lines = len(universe)
    cols = len(universe[0])

    # expand universe, lines first
    line_has_contents = True
    append = False
    for l in range(lines - 1, -1, -1):
        if not line_has_contents:
            newline = '.' * cols
            universe.insert(l + 1, newline)
            lines += 1

        line_has_contents = False
        for c in range(cols - 1, -1, -1):
            if universe[l][c] != '.':
                line_has_contents = True

    # expand universe width
    column_has_contents = True
    for c in range(cols - 1, -1, -1):
        if not column_has_contents:
            append = True
            cols += 1

        column_has_contents = False
        for l in range(lines - 1, -1, -1):
            if universe[l][c] != '.':
                column_has_contents = True
            if append:
                universe[l] = universe[l][0:c + 1] + '.' + universe[l][c + 1:]
        append = False

    for line in universe:
        print(line)

    # Get coordinates for each galaxy
    galaxies = []

    for l in range(lines):
        for c in range(cols):
            if universe[l][c] == '#':
                galaxies.append((l, c))

    print(galaxies)

    lengths = []

    for i, g in enumerate(galaxies):
        for other_galaxy in galaxies[i + 1:]:
            lengths.append(get_distance(g, other_galaxy))

    print(lengths)
    print(len(lengths))
    print(sum(lengths))
    return 0


empty_lines = []
empty_cols = []


def get_distance(galaxy1, galaxy2):
    # (1, 1), (2, 2)
    FILL_FACTOR = 1000000-1
    line_add = 0
    column_add = 0

    if galaxy1[0] > galaxy2[0]:
        line_distance_start = galaxy2[0]
        line_distance_end = galaxy1[0]
    else:
        line_distance_start = galaxy1[0]
        line_distance_end = galaxy2[0]

    # go through each line between start and end and if there are blanks add FILL_FACTOR
    for current_line in range(line_distance_start, line_distance_end):
        if current_line in empty_lines:
            line_add += FILL_FACTOR

    # columns
    if galaxy1[1] > galaxy2[1]:
        column_distance_start = galaxy2[1]
        column_distance_end = galaxy1[1]
    else:
        column_distance_start = galaxy1[1]
        column_distance_end = galaxy2[1]

    # go through each column between start and end and if there are blanks add FILL_FACTOR
    for current_col in range(column_distance_start, column_distance_end):
        if current_col in empty_cols:
            column_add += FILL_FACTOR

    line = line_distance_end - line_distance_start + line_add
    column = column_distance_end - column_distance_start + column_add

    return line + column


def day11b():
    global universe, empty_lines, empty_cols
    with open("day11.txt") as myfile:
        universe = myfile.read().split('\n')

    lines = len(universe)
    cols = len(universe[0])

    # expand universe, lines first
    line_has_contents = True
    append = False
    for l in range(lines):
        if not line_has_contents:
            empty_lines.append(l - 1)

        line_has_contents = False
        for c in range(cols):
            if universe[l][c] != '.':
                line_has_contents = True

    # expand universe width
    column_has_contents = True
    for c in range(cols):
        if not column_has_contents:
            empty_cols.append(c - 1)
        column_has_contents = False
        for l in range(lines):
            if universe[l][c] != '.':
                column_has_contents = True

    # for line in universe:
    #     print(line)

    print(f"empty_cols: {empty_cols}")
    print(f"empty_lines:{empty_lines}")

    # Get coordinates for each galaxy
    galaxies = []

    for l in range(lines):
        for c in range(cols):
            if universe[l][c] == '#':
                galaxies.append((l, c))

    # print(galaxies)

    lengths = []

    for i, g in enumerate(galaxies):
        for other_galaxy in galaxies[i + 1:]:
            lengths.append(get_distance(g, other_galaxy))

    # print(lengths)
    # print(len(lengths))
    print(sum(lengths))
    return 0


if __name__ == '__main__':
    res = day11b()
    print(res)
    #
    # mystring = "I_am_a_fish"
    # words = mystring.split('_')
    # pattern = re.compile(r'[-_,]')
    # words = re.split(pattern, mystring)
    # print(words, mystring)
    # mylist = []
    # for i, w in enumerate(words):
    #     if i > 0:
    #         for index, letter in enumerate(w):
    #             if index == 0:
    #                 mylist.append(letter.upper())
    #             else:
    #                 mylist.append(letter)
    #
    # mylist.insert(0,words[0])
    # print("".join( mylist))
