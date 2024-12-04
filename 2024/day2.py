import itertools
from itertools import count


def safe_list(list):
    l = len(list)
    for id, item in enumerate(list[:-1]):

        # Early exit for same
        diff = list[id+1]-item
        if diff ==0:
            return False

        # first run
        if id ==0:
            if diff > 0:
                ascending = True
            elif diff < 0:
                ascending = False

        if ascending:
            if 0 < diff <=3:
                continue
            else:
                return False
        else:
            if -3 <= diff < 0:
                continue
            else:
                return False
    return True


def day2a():
    safe = 0
    unsafe = 0

    left = []
    right = []
    with open("day2.txt") as inputfile:
        for line in inputfile.readlines():
            line_list = [int(a) for a in line.split()]
            if safe_list(line_list):
                safe+=1
            else:
                unsafe+=1
    return safe

def safe_list_damp(list):
    l = len(list)
    line_safe = 0
    safes = []
    for i in range(l):
        new_list = list[:]
        new_list.pop(i)
        safes.append(safe_list(new_list))
    z = safes.count(True)
    if z > 0:
        return True
    return False

    # for id, item in enumerate(list[:-1]):
    #
    #     # Early exit for same
    #     diff = list[id+1]-item
    #     if diff ==0:
    #         line_safe+=1
    #         continue
    #
    #     if id ==1 and line_safe:
    #         ascending = None
    #     # first run
    #     if ascending is None:
    #         if diff > 0:
    #             ascending = True
    #         elif diff < 0:
    #             ascending = False
    #
    #     if ascending:
    #         if 0 < diff <=3:
    #             continue
    #         else:
    #             line_safe+=1
    #             continue
    #     else:
    #         if -3 <= diff < 0:
    #             continue
    #         else:
    #             line_safe+=1
    #             continue
    # if line_safe < 2:
    #
    #     return True
    # else:
    #     print(list)
    #     return False

def day2b():
    safe = 0
    unsafe = 0

    with open("day2.txt") as inputfile:
        for line in inputfile.readlines():
            line_list = [int(a) for a in line.split()]
            if safe_list_damp(line_list):
                safe+=1
            else:
                unsafe+=1
    return safe




if __name__ == '__main__':
    res = day2b()
    print(res)