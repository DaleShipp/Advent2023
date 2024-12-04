from collections import defaultdict


def day1a():
    left = []
    right = []
    with open("day1.txt") as inputfile:
        for line in inputfile.readlines():
            a,b = line.split()
            # print(line,a,b)
            left.append(int(a))
            right.append(int(b))

    sleft = sorted(left)
    sright = sorted(right)

    combined = zip(sleft, sright)
    total = 0
    for a,b in combined:
        if a > b:
            diff = a-b
        else:
            diff = b-a
        total += diff


    return total

def day1b():
    left = []
    right = []
    with open("day1.txt") as inputfile:
        for line in inputfile.readlines():
            a,b = line.split()
            # print(line,a,b)
            left.append(int(a))
            right.append(int(b))
    total = 0
    counts = defaultdict(int)
    for a in left:
        for b in right:
            if a==b:
                counts[a]+=1

    for a in left:
        total += counts[a]* a

    # print(counts)



    return total

if __name__ == '__main__':
    res = day1b()
    print(res)