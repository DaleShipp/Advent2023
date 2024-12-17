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
            total += int(pages[l//2])
    return total


if __name__ == '__main__':
    res = day5a()
    print(res)