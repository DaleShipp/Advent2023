import math


def score_calculate(hold_time, distance, total_time):
    return hold_time * (total_time - hold_time) > distance


def score_races(time, distance):
    pass_count = 0
    remainder = time % 2
    #  if its an odd number, there are an even number of answers surrounding the middle
    #  if its even there are an odd number including the half point
    end = time // 2
    for i in range(end + 1):
        if score_calculate(i, distance, time):
            pass_count += 2
    return pass_count - (1 - remainder)


def sub():
    with open("day6.txt") as myfile:
        contents = myfile.readlines()
        t, d = contents[0].strip(), contents[1].strip()
        time_list = [i for i in t.split(' ') if i]
        dist_list = [i for i in d.split(' ') if i]
        total = []
        for i in range(len(time_list) - 1):
            total.append(score_races(int(time_list[i + 1]), int(dist_list[i + 1])))

    return math.prod(total)


if __name__ == '__main__':
    res = sub()
    print(res)
