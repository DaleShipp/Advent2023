import math
from string import digits


def get_symbol_positions(line):
    sym_list = []
    for i, c in enumerate(line):
        if c != '.' and c not in digits:
            sym_list.append(i)
    return sym_list


def check_part_number(line_number, position, number, symbol_array):
    l = len(number)
    valid_positions = set(range(position - 1 - l, position + 1))

    # line before
    if line_number > 0:
        check_line = set(symbol_array[line_number - 1])
        if valid_positions & check_line:
            return True

    # same line
    check_line = set(symbol_array[line_number])
    if valid_positions & check_line:
        return True

    # line after
    if line_number + 1 in symbol_array:
        check_line = set(symbol_array[line_number + 1])
        if valid_positions & check_line:
            return True
        
    return False


def day3_a():
    symbol_array = dict()

    with open('day3.txt') as myfile:
        for ln, line in enumerate(myfile):
            # for each line in the file work out the symbol positions
            symbol_array[ln] = (get_symbol_positions(line.strip()))

        print(symbol_array)
        parts = list()
        myfile.seek(0)
        for ln, line in enumerate(myfile):
            line = line.strip()
            max_l = len(line)

            cnum = ''
            for i, c in enumerate(line):
                if c in digits:
                    cnum += c
                    if i == max_l - 1:
                        if check_part_number(ln, i, cnum, symbol_array):
                            parts.append(int(cnum))
                            cnum = ''
                else:
                    if cnum:
                        if check_part_number(ln, i, cnum, symbol_array):
                            parts.append(int(cnum))
                        cnum = ''

    return sum(parts)


symbol_array = dict()
gear_array = dict()


def get_gear_positions(line):
    sym_list = []
    for i, c in enumerate(line):
        if c == '*':
            sym_list.append(i)
    return sym_list


def hang_number(line_number, valid_positions, number):
    """Hangs the number off the adjacent gear in a dictionary
    gears are indexed by line number and position, so gear on line 9 with position 65 is '9|65'"""
    global gear_array
    check_line = set(symbol_array[line_number])
    for a in valid_positions & check_line:
        try:
            gear_array[str(line_number) + '|' + str(a)] += [int(number)]
        except KeyError:
            gear_array[str(line_number) + '|' + str(a)] = [int(number)]


def hang_number_if_adjacent(line_number, position, number):
    global symbol_array, gear_array
    l = len(number)

    valid_positions = set(range(position - 1 - l, position + 1))

    # line before
    if line_number > 0:
        hang_number(line_number - 1, valid_positions, number)

    # current line
    hang_number(line_number, valid_positions, number)

    # line after
    if line_number + 1 in symbol_array:
        hang_number(line_number + 1, valid_positions, number)


def day3_b():
    global symbol_array, gear_array
    with open('day3.txt') as myfile:
        for ln, line in enumerate(myfile):
            # for each line in the file work out the gear positions
            symbol_array[ln] = (get_gear_positions(line.strip()))

        # initialise everything
        myfile.seek(0)
        check_num = False

        # build dictionary of numbers for each gear
        for ln, line in enumerate(myfile):
            line = line.strip()
            max_l = len(line)

            cnum = ''
            for i, c in enumerate(line):
                if c in digits:
                    cnum += c
                    if i == max_l - 1:
                        check_num = True
                else:
                    if cnum:
                        check_num = True

                if check_num:
                    hang_number_if_adjacent(ln, i, cnum)
                    cnum = ''

                    check_num = False

    total = 0
    # for each gear with multiple numbers add the ratio
    for k,v in gear_array.items():
        if len(v)>1:
            total += math.prod(v)
    return total


if __name__ == '__main__':
    result = day3_b()
    print(result)
