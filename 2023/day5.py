from functools import cache
from itertools import pairwise

def day5a():
    total = []

    with open("day5.txt", encoding="utf-8") as file:
        contents = file.read()
        segments = contents.split('\n\n')
        seeds = map(int, segments[0].split(' ')[1:])

        clean_segments = []
        # Format: start1, end1, start2, end2, len
        for seg in segments[1:]:
            seglist = []
            rows = seg.split('\n')
            name = rows.pop(0)
            for row in rows:
                a, b, c = map(int, row.split(' '))
                seglist.append([b, b + c, a, a + c, c])
            # pre-process segments
            clean_segments.append(seglist)

        # loop through each map set and change seed into destination
        for s, seed in enumerate(seeds):
            for seg in clean_segments:
                # see if any of the ranges are for the seed, if so map the new number
                filtered_seg = list(filter(lambda x: x[0] <= seed and x[1] >= seed, seg))
                if filtered_seg:
                    seed += filtered_seg[0][2] - filtered_seg[0][0]
            total.append(seed)
    return min(total)



clean_segments = []

@cache
def get_seed(number, range, seg):


    global clean_segments

    for a, b, c in clean_segments[seg]:
        if a <= number <= a + c:
            if a<= number + range <= a + c:

                if seg > 0:
                    seed = get_seed(b-a+number, b-a+number+range , seg - 1)
                else:
                    seed =b-a+number
            return seed
    else:
        if seg > 0:
            return get_seed(number,seg-1)
        else:
            return number


def day5b():
    global clean_segments

    with open("day5t.txt", encoding="utf-8") as file:
        contents = file.read()
    segments = contents.split('\n\n')
    seeds = list(map(int, segments[0].split(' ')[1:]))
    pairseeds = list(pairwise(seeds))[::2]
    # Format: start1, end1, start2, end2, len - clean up the segment data

    for seg in segments[1:]:
        seglist = []
        rows = seg.split('\n')
        name = rows.pop(0)
        for row in rows:
            a, b, c = map(int, row.split(' '))
            seglist.append([a, b, c])
        # pre-process segments
        clean_segments.append(seglist)

    mins = []
    # find the minimum location and go from there

        i = 0
        while True:
            i+=1
            # if i %1000000 ==0:
            #     print(i, sep='', end=',')
            s = get_seed(i, 6)
            if s:
                for p in pairseeds:
                    if p[0] <= s <= p[0] + p[1]:
                        return (i)
    print(mins)
    return min(mins)
# umber 82, which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46.

if __name__ == '__main__':
    import time

    start = time.time()
    res = day5b()
    end = time.time()
    print(end - start)
    print(res)
