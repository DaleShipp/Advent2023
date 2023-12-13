from itertools import pairwise

import math

MAX_LEN = 0
def extrapolate_next(contents):
    global MAX_LEN
    r = []
    loops = 0
    r.append(contents)
    current_line = contents
    # Build list pyramid
    while sum(r[loops]) != 0 or math.prod(r[loops]) != 0:
        loops += 1
        current_line = [b - a for a, b in pairwise(current_line)]
        r.append(current_line)

    MAX_LEN = max(MAX_LEN,len(r))
    # for each line of r, get next value
    last_val = 0
    while len(r) > 1:
        current_line = r.pop(-1)
        last_val = current_line[-1]
        next_val = last_val + r[-1][-1]
        r[-1].append(next_val)

    return next_val

def day9a():
    total = 0
    for line in open("day9.txt"):
        contents = [int(i) for i in line.strip().split(' ') if i]
        nextval = extrapolate_next(contents)
        total += nextval
    return total

def day9b():
    total = 0
    for line in open("day9.txt"):
        contents = [int(i) for i in line.strip().split(' ') if i]
        nextval = extrapolate_next(contents[::-1])
        total += nextval
    return total

if __name__ == '__main__':
    res = day9b()
    print(res)
    print(MAX_LEN)
