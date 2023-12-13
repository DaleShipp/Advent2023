from itertools import pairwise
from threading import Thread


def day5a():
    seeds = []

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


def fracture_seeds(p, q, clean_segments, resultdict):
    total = []

    # Format: start1, end1, start2, end2, len - clean up the segment data
    seed = [p, q]
    res_dict = {}

    # loop through each map set and change seed into destination

    for seg in clean_segments:
        # full containment
        filtered_seg = list(filter(lambda x: x[0] <= p and x[1] >= q, seg))
        if filtered_seg:
            p += filtered_seg[0][2] - filtered_seg[0][0]
            q += filtered_seg[0][2] - filtered_seg[0][0]
        else:
        # start in
            filtered_seg = list(filter(lambda x: x[0] <= q and x[1] > q, seg))
            for x in filtered_seg:
                fracture_seeds(x[0],q,clean_segments, res_dict)

            # end in
            filtered_seg = list(filter(lambda x: x[0] <=p  and x[1] > p, seg))
            for x in filtered_seg:
                fracture_seeds(p,x[1],clean_segments, res_dict)
    for k, v in res_dict.items():
        for i in v:
            total.extend([i])

    total.extend(seed)

    resultdict[p] = total
    return


def expand_seeds(p, q, clean_segments, resultdict):
    total = []
    print("Processing {}".format(p))
    seeds = [s for s in range(p, p + q)]

    # loop through each map set and change seed into destination
    for s, seed in enumerate(seeds):
        for seg in clean_segments:
            # see if any of the ranges are for the seed, if so map the new number
            filtered_seg = list(filter(lambda x: x[0] <= seed and x[1] >= seed, seg))
            if filtered_seg:
                seed += filtered_seg[0][2] - filtered_seg[0][0]
        total.append(seed)

    resultdict[p] = total
    return


def day5b():
    seeds = []
    total = []

    with open("day5.txt", encoding="utf-8") as file:
        contents = file.read()
        segments = contents.split('\n\n')
        seeds = list(map(int, segments[0].split(' ')[1:]))
        pairseeds = list(pairwise(seeds))[::2]

        # Format: start1, end1, start2, end2, len - clean up the segment data
        clean_segments = []
        for seg in segments[1:]:
            seglist = []
            rows = seg.split('\n')
            name = rows.pop(0)
            for row in rows:
                a, b, c = map(int, row.split(' '))
                seglist.append([b, b + c, a, a + c, c])
            # pre-process segments
            clean_segments.append(seglist)

        threads = []
        result_dict = dict()

        for p, q in pairseeds:
            # fracture_seeds(p,p+q,clean_segments,result_dict)
            t = Thread(target=expand_seeds, args=(p, q, clean_segments, result_dict,))
            threads.append(t)
            t.start()
 

        for thread in threads:
            thread.join()
            print(f"Finished {thread}")

        print(result_dict)
        for k, v in result_dict.items():
            total += v

    return min(total)


if __name__ == '__main__':
    import time

    start = time.time()
    res = day5b()
    end = time.time()
    print(end - start)
    print(res)
