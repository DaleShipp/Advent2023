import math

def day_two_a():
    result = 0
    maximums = {'blue': 14,
                'red': 12,
                'green': 13}

    for i, line in enumerate(open("day2.txt")):
        l = len(line)
        s = line[5:]
        n_str, g_str = s.split(':')
        game_list = g_str.split(';')

        v = check_viable(game_list, maximums)
        if v:
            result += int(n_str)
    return result


def check_viable(game_list, maximums):
    games = {}
    for i, game in enumerate(game_list):
        rounds = {}
        r = game.split(',')
        for round in r:
            current = round.strip().split(' ')
            rounds[current[1]] = current[0]
            if int(current[0]) > maximums[current[1]]:
                return False

        games[i] = rounds
    print(games)
    return True


def get_product(game_list, maximums):
    rounds = {}
    for i, game in enumerate(game_list):
        r = game.split(',')
        for round in r:
            current = round.strip().split(' ')
            try:
                if int(current[0]) > rounds[current[1]]:
                    rounds[current[1]] = int(current[0])
            except:
                rounds[current[1]] = int(current[0])

    s = math.prod([int(v) for k, v in rounds.items()])
    return s


def day_two_b():
    result = 0
    maximums = {'blue': 14,
                'red': 12,
                'green': 13}

    for i, line in enumerate(open("day2.txt")):
        l = len(line)
        s = line[5:]
        n_str, g_str = s.split(':')
        game_list = g_str.split(';')
        v = get_product(game_list, maximums)
        result += v
    return result


if __name__ == '__main__':
    res = day_two_b()
    print(res)
