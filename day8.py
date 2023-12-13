import re

def day8a():
    total = 0
    mapdict = {}
    with open("day8.txt") as myfile:
        contents = myfile.read()
        instructions, rest = contents.split('\n\n')
        lines = rest.split('\n')
        pattern = re.compile(r'[=\s(),]')
        for line in lines:
            split_string = [i for i in list(re.split(pattern, line)) if i]

            mapdict[split_string[0]] = tuple(split_string[1:])

    #     process the instruction list
    count = 0
    l = len(instructions)
    current = 'AAA'
    while current != 'ZZZ':
        if instructions[count % l] == 'L':
            current = mapdict[current][0]
        else:
            current = mapdict[current][1]
        count += 1
    return count


mapdict = {}


def day8b():
    total = 0
    global mapdict
    with open("day8.txt") as myfile:
        contents = myfile.read()
        instructions, rest = contents.split('\n\n')
        lines = rest.split('\n')
        pattern = re.compile(r'[=\s(),]')
        for line in lines:
            split_string = [i for i in list(re.split(pattern, line)) if i]
            mapdict[split_string[0]] = tuple(split_string[1:])

    #     process the instruction list
    count = 0
    l = len(instructions)
    factors = []
    # iterate over list and record count every time there is a Z end - these are our factors
    current = [a for a in mapdict.keys() if a[2] == 'A']
    while True:
        for i in current:
            if i[2] == 'Z':
                factors.append(count)
                current.remove(i)
        if current:
            if instructions[count % l] == 'L':
                current = [mapdict[i][0] for i in current]
            else:
                current = [mapdict[i][1] for i in current]
        else:
            break
        count += 1

    # for each factor (end point) get the remainder against multiples of the largest to calculate
    # lowest common multiple
    max_factor = factors[-1]
    multiple = 1
    while True:
        remainders = []
        for i in factors:
            remainders.append( (max_factor*multiple) % i)
        if sum(remainders) ==0:
            break
        multiple+=1

    return multiple*max_factor


if __name__ == '__main__':
    res = day8b()
    print(res)
