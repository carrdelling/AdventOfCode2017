

def rotate(pattern):

    size = len(pattern)

    new_p = []

    for x in range(size):
        row = [pattern[y][x] for y in range(size)]
        new_p.append("".join(row))

    return tuple(new_p)


def expand_rules(rules):

    # expand pattern first
    for k, v in list(rules.items()):

        # add all flips
        new_k = tuple([x[::-1] for x in k])
        rules[new_k] = v

        new_k = tuple(s for s in k[::-1])
        rules[new_k] = v

        new_k = tuple([s[::-1] for s in new_k])
        rules[new_k] = v

    # add rotations too!
    for k, v in list(rules.items()):
        new_k = rotate(k)
        rules[new_k] = v

    return rules


def solve(data):

    STEPS = 5
    INITIAL = [
        ".#.",
        "..#",
        "###",
    ]

    rules = expand_rules(data)
    grid = list(INITIAL)

    for _ in range(STEPS):

        new_grid = []

        # break into 2x2, make them 3x3
        if len(grid) % 2 == 0:
            for y in range(0, len(grid), 2):
                # 3 output rows
                new_fragment = {0: [],
                                1: [],
                                2: []}
                for x in range(0, len(grid), 2):
                    pattern = tuple([grid[y][x:x + 2], grid[y + 1][x:x + 2]])
                    v = rules[pattern]
                    for idx, l in enumerate(v):
                        new_fragment[idx] += list(l)
                new_grid += ["".join(new_fragment[line]) for line in sorted(new_fragment)]
        # break into 3x3, make them 4x4
        elif len(grid) % 3 == 0:
            for y in range(0, len(grid), 3):
                new_fragment = {0: [],
                                1: [],
                                2: [],
                                3: []}
                for x in range(0, len(grid), 3):
                    k = tuple([grid[y][x:x + 3], grid[y + 1][x:x + 3], grid[y + 2][x:x + 3]])
                    v = rules[k]
                    for idx, l in enumerate(v):
                        new_fragment[idx] += list(l)
                new_grid += ["".join(new_fragment[line]) for line in sorted(new_fragment)]
        else:
            assert False, ("Size error", len(grid))
        grid = list(new_grid)

    solution = 0

    for row in grid:
        solution += sum([1 if c == "#" else 0 for c in row])

    return solution


def main():

    data = {}
    with open('input') as in_f:
        for row in in_f:
            k, v = row.strip().split(" => ")
            k = tuple(k.split("/"))
            v = v.split("/")

            data[k] = v

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
