import re

test_string = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

def day3a():
    pattern = r"mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)"
    r = re.compile(pattern)
    total = 0

    with open("day3.txt") as inputfile:
        for line in inputfile.readlines():
            operations = r.findall(line)

            for op in operations:
                comma = op.find(',')
                a = int(op[4:comma])
                b = int(op[comma+1:-1])
                total += a*b
    return total

def day3b2():
    import re
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, open("day3.txt").read())
    res = 0
    flag = True
    # print(matches)
    for match in matches:
        # print(match)
        if match == "do()":
            flag = True
            # print(1)
        elif match == "don't()":
            flag = False
            # print(0)
        else:
            if flag:
                x, y = map(int, match[4:-1].split(","))
                res += x * y
    return res


def day3b():
    pattern = r"mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)"
    # inactive_pattern = r"don\'t\(\).*do\(\)"
    r = re.compile(pattern)
    total = 0

    test = f"xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

    with open("day3.txt") as inputfile:
        line = inputfile.read()
            # cline = test
        cline = line

        # Clean it
        print(cline)
        while True:
            pos = cline.find(f"don't()")
            if pos >= 0:
                pos2 = cline.find('do()',pos)
                if pos2 >= 0:
                    print(pos, pos2)
                    cline = cline[:pos] + cline[pos2+4:]
                else:
                    # pos2 = len(line)
                    cline = cline[:pos]
            if -1 in (pos,pos2):
                break

        print("cleaned", cline)

        operations = r.findall(cline)
        print(operations)

        for op in operations:
            comma = op.find(',')
            a = int(op[4:comma])
            b = int(op[comma+1:-1])
            total += a*b
            # print(a,b)
        # break
    return total


if __name__ == '__main__':
    res = day3b()
    print(res)
    res = day3b2()
    print(res)