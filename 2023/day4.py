import math
from functools import lru_cache

def day4a():
    with open("day4.txt", encoding="utf-8") as file:
        contents = file.readlines()
        total = 0
        for line in contents:
            card, numbers = line.split(':') # split the Card numbers and data
            win_nums, entry_nums = numbers.split(' | ')

            # put the  numbers into two sets of integers
            win_set = frozenset([int(i) for i in win_nums.strip().split(' ') if i.isdigit()])
            entry_set = frozenset([int(i) for i in entry_nums.strip().split(' ') if i.isdigit()])

            # Winning numbers are the set union of the two sets
            winners = win_set & entry_set

            # The score is 2 raised to the power of the count-1
            score = int(math.pow(2,len(winners)-1))
            total += score
    return total

contents = ""

@lru_cache()
def score_card(line_num, line):
    global contents
    score = 1
    card, numbers = line.split(':')
    win_nums, entry_nums = numbers.split(' | ')
    win_set = frozenset([int(i) for i in win_nums.strip().split(' ') if i.isdigit()])
    entry_set = frozenset([int(i) for i in entry_nums.strip().split(' ') if i.isdigit()])

    # Winning numbers are the set union of the two sets
    winners = win_set & entry_set
    won = len(winners)

    for i in range(won):
        score += score_card(line_num+1+i, contents[line_num+1+i])

    return score

def day4b():
    global contents
    with open("day4.txt", encoding="utf-8") as file:
        contents = file.readlines()
        total = 0
        for lno, line in enumerate(contents):
            score = score_card(lno,line)
            total += score
    return total


if __name__ == '__main__':
    import time
    start = time.time()
    res = day4b()
    end = time.time()
    print(end-start)
    print(res)
