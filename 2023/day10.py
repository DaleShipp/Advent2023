from itertools import pairwise

import math

MAX_LEN = 0

universe = 0

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S

direction_map = {
    '|': [(0, 1), (0, -1)],
    '-': [(1, 0), (-1, 0)],
    'L': [(0, -1), (1, 0)],
    'J': [(0, -1), (-1, 0)],
    '7': [(0, 1), (-1, 0)],
    'F': [(0, 1), (1, 0)],
}

def points_to(param):
    global universe
    x = param[0]
    y = param[1]
    sign = contents[y][x]
    try:
        points = direction_map[sign]
        translated_points = {(x + points[0][0], y + points[0][1]), (x + points[1][0], y + points[1][1])}
        return translated_points
    except KeyError:
        return {}


def day10a():
    global universe
    startpos = ()
    with open("day10.txt") as myfile:
        contents = myfile.read().split('\n')

    lines = len(contents)
    cols = len(contents[0])

    # find Startpos
    for i in range(lines):
        p = contents[i].find('S')
        if p > -1:
            startpos = (p, i)
            break

    total = 0
    last_value = startpos
    next_value = startpos
    # Follow the path - what connects to S
    startx = max(startpos[0] - 1,0)
    endx = min(startpos[0] + 1,cols)
    starty = max(startpos[1] - 1,0)
    endy = min(startpos[1] + 1,lines)
    for x in range(startx, endx +1):
        for y in range(starty, endy+1):
            if startpos in points_to((x, y)):
                last_value = startpos
                next_value = (x, y)
                total += 1
                break

    while next_value != startpos:
        viable  = points_to(next_value)
        current = viable - {last_value}
        last_value = next_value
        next_value = current.pop()
        total+=1

    return total//2


if __name__ == '__main__':
    res = day10a()
    print(res)
