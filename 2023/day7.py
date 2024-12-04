import collections
import functools
import math
from contextlib import suppress


# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456

# else:  # They are equal
# if ranks.index(left[i][0]) < ranks.index(right[i][0]):
#     return 1
# elif ranks.index(left[i][0]) > ranks.index(right[i][0]):
#     return -1

def card_greater(left_hand, right_hand):
    ranks = ('A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2')
    left = collections.Counter(left_hand[0]).most_common()
    right = collections.Counter(right_hand[0]).most_common()

    min_range = min(len(left), len(right))

    # compare counts
    for i in range(min_range):
        if left[i][1] > right[i][1]:
            return 1
        elif left[i][1] < right[i][1]:
            return -1

    # counts are same so compare individual ranks
    for i in range(5):
        if ranks.index(left_hand[0][i]) < ranks.index(right_hand[0][i]):
            return 1
        elif ranks.index(left_hand[0][i]) > ranks.index(right_hand[0][i]):
            return -1
    return 0


def card_greaterb(left_hand, right_hand):
    ranks = ('A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J')
    l_ctr = collections.Counter(left_hand[0])
    r_ctr = collections.Counter(right_hand[0])

    # compare counts
    l_count = r_count = 0
    with suppress(KeyError):
        l_count = l_ctr['J']
        r_count = r_ctr['J']
        del l_ctr['J']
        del r_ctr['J']

    if len(l_ctr) == 0:
        l_ctr = collections.Counter(left_hand[0])
        l_count = 0
    if len(r_ctr) == 0:
        r_ctr = collections.Counter(right_hand[0])
        r_count = 0
    left = l_ctr.most_common()
    right = r_ctr.most_common()
    min_range = min(len(left), len(right))

    # if 'J' == left[0][0]:
    #     try:
    #         l_ctr[left[1][0]] += l_ctr['J']
    #         del l_ctr['J']
    #     except:
    #         pass
    # if 'J' == right[0][0]:
    #     try:
    #         r_ctr[right[1][0]] += r_ctr['J']
    #         del r_ctr['J']
    #     except:
    #         pass
    #
    #
    # left = l_ctr.most_common()
    # right = r_ctr.most_common()
    #
    # min_range = min(len(left), len(right))

    # compare counts
    for i in range(min_range):
        if i==0:
            if left[i][1] + l_count > right[i][1] + r_count:
                return 1
            elif left[i][1] + l_count < right[i][1] + r_count:
                return -1
        else:
            if left[i][1] > right[i][1]:
                return 1
            elif left[i][1] < right[i][1]:
                return -1

    # counts are same so compare individual ranks
    for i in range(5):
        if ranks.index(left_hand[0][i]) < ranks.index(right_hand[0][i]):
            return 1
        elif ranks.index(left_hand[0][i]) > ranks.index(right_hand[0][i]):
            return -1
    return 0


def sub():
    total = 0
    hands = []
    for line in open("day7.txt"):
        hand = tuple(line.strip().split(' '))
        hands.append(hand)

    sortedhands = sorted(hands, key=functools.cmp_to_key(card_greaterb))
    print(([i[0] for i in sortedhands][::-1]))

    for i, hand in enumerate(sortedhands):
        total += int(hand[1]) * (i + 1)

    return total


if __name__ == '__main__':
    res = sub()
    print(res)

# 246609948
