from string import digits

def day_one_a():
    digitset = frozenset(digits)
    result = 0

    for line in open("day1.txt"):
        number_string = ''.join(i for i in line if i in digitset)
        result += int(number_string[0] + number_string[-1])
    return result

numbers = {'eight': "8",
           'seven': "7",
           'nine': "9",
           'five': "5",
           'four': "4",
           'three': "3",
           'two': "2",
           'one': "1",
           'six': "6",
           }

def match_first(param: str, reverse=False):
    digitset = frozenset(digits)
    accum = ""
    l = len(param)
    for i in range(l):
        checkword = param[:i + 1]
        for n in digitset:
            if n in checkword:
                return n

        for a, b in numbers.items():
            if reverse: a = "".join(reversed(a))
            if a in checkword:
                return b
    return accum

def day_one_b():
    result = 0

    for line in open("day1.txt"):
        l = line.rstrip()
        r = "".join(reversed(l))

        firstdigit = match_first(l)
        lastdigit = match_first(r,True)
        inc = int(str(firstdigit) + str(lastdigit))
        result += inc
    return result


if __name__ == '__main__':
    res = day_one_b()
    print(res)
