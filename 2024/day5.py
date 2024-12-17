from collections import defaultdict


def day5a():
    rules = defaultdict(set)
    changes = []
    rules_flag = True
    with open("day5.txt") as inputfile:
        table = inputfile.read().split()
        for row in table:

            # Are we reading rules or changes
            if rules_flag:
                try:
                    a, b = row.split('|')

                    # Add the rule to a dict keyed by the X page
                    rules[a].add(b)
                    continue
                except:
                    rules_flag = False

            # We are in the changes section
            changes.append(row)

    # Iterate over all changes
    failed_rows = 0
    total = 0
    for row in changes:
        pages = row.split(',')
        failed_pages = 0
        pages_seen = set()
        for page in pages:
            if pages_seen.intersection(rules[page]):
                failed_pages += 1

            pages_seen.add(page)

        if failed_pages:
            failed_rows += 1
        else:
            l = len(pages)
            total += int(pages[l // 2])
    return total


def reformat_row(pages, rules):
    valid = False
    while not valid:
        pages_seen = set()
        valid = True
        for i, page in enumerate(pages):
            broken = pages_seen.intersection(rules[page])
            if broken:
                valid = False
                loc = pages.index(broken.pop())
                v = pages.pop(loc)
                pages.insert(i, v)
                continue

            pages_seen.add(page)

    return pages


def day5b():
    rules = defaultdict(set)
    changes = []
    rules_flag = True
    with open("day5.txt") as inputfile:
        table = inputfile.read().split()
        for row in table:

            # Are we reading rules or changes
            if rules_flag:
                try:
                    a, b = row.split('|')

                    # Add the rule to a dict keyed by the X page
                    rules[a].add(b)
                    continue
                except:
                    rules_flag = False

            # We are in the changes section
            changes.append(row)

    # Iterate over all changes
    failed_rows = []
    total = 0
    failtotal = 0
    for row in changes:
        pages = row.split(',')
        failed_pages = []
        pages_seen = set()
        for index, page in enumerate(pages):
            if pages_seen.intersection(rules[page]):
                failed_pages.append(index)

            pages_seen.add(page)

        l = len(pages)

        if failed_pages:
            failed_rows.append(pages)
            pages = reformat_row(pages, rules)
            failtotal += int(pages[l // 2])
        else:
            total += int(pages[l // 2])
    return total, failtotal


if __name__ == '__main__':
    res = day5a()
    print(res)
    res = day5b()
    print(res)
