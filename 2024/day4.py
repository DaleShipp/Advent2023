def check_valid(table, rnum, colnum):
    directions = [
        [(rnum - 1, colnum), (rnum - 2, colnum), (rnum - 3, colnum)],
        [(rnum - 1, colnum + 1), (rnum - 2, colnum + 2), (rnum - 3, colnum + 3)],
        [(rnum, colnum + 1), (rnum, colnum + 2), (rnum, colnum + 3)],
        [(rnum + 1, colnum + 1), (rnum + 2, colnum + 2), (rnum + 3, colnum + 3)],
        [(rnum + 1, colnum), (rnum + 2, colnum), (rnum + 3, colnum)],
        [(rnum + 1, colnum - 1), (rnum + 2, colnum - 2), (rnum + 3, colnum - 3)],
        [(rnum, colnum - 1), (rnum, colnum - 2), (rnum, colnum - 3)],
        [(rnum - 1, colnum - 1), (rnum - 2, colnum - 2), (rnum - 3, colnum - 3)]
    ]

    valid = 0

    for d in directions:
        try:
            mr,mc = d[0]
            ar,ac = d[1]
            sr,sc = d[2]

            # Bounds checking
            if mr < 0 or mc < 0 or ar < 0 or ac < 0 or sr < 0 or sc < 0:
                continue

            if table[mr][mc]=='M' and table[ar][ac]=='A' and table[sr][sc]=='S':
                valid +=1

        except:
            pass
    return valid


def day4a():
    total = 0
    with open("day4.txt") as inputfile:
        table = inputfile.read().split()
        for rnum, row in enumerate(table):
            for colnum, char in enumerate(row):
                if char == 'X':
                    valid = check_valid(table, rnum, colnum)
                    if valid:
                        total += valid
    return total

def check_valid2(table, rnum, colnum):
    directions = [
        [(rnum - 1, colnum - 1),  (rnum +1 , colnum + 1)],
        [(rnum - 1, colnum + 1), (rnum + 1, colnum - 1)],
    ]

    valid = 0

    for d in directions:
        try:
            mr,mc = d[0]
            sr,sc = d[1]

            # Bounds checking
            if mr < 0 or mc < 0 or sr < 0 or sc < 0:
                continue

            if table[mr][mc]=='M' and table[sr][sc]=='S' or table[mr][mc]=='S' and table[sr][sc]=='M':
                valid +=1

        except:
            pass
    return valid > 1


def day4b():
    total = 0
    with open("day4.txt") as inputfile:
        table = inputfile.read().split()
        for rnum, row in enumerate(table):
            for colnum, char in enumerate(row):
                if char == 'A':
                    valid = check_valid2(table, rnum, colnum)
                    if valid:
                        total += 1
    return total

if __name__ == '__main__':
    res = day4b()
    print(res)
