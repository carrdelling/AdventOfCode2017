from itertools import product
from collections import defaultdict


def encrypt(keys, data, current=0, skip=0):

    size = len(data)

    for k in keys:

        subchain = [data[(current+ii) % size] for ii in range(k)][::-1]
        for ii in range(k):
            idx = (current+ii) % size
            data[idx] = subchain[ii]

        # move current
        current += k + skip
        current = current if current < size else current - size

        # increase skip
        skip += 1

    return data, current, skip


def knot_hash(data):

    ascii = [ord(x) for x in data]
    keys = ascii + [17, 31, 73, 47, 23]

    data = list(range(256))
    data, current, skip = encrypt(keys, data)

    for r in range(63):
        data, current, skip = encrypt(keys, data, current, skip)

    dense = []
    for offset in range(16):
        keys = data[16*offset:(16*offset) + 16]

        xor = keys[0]
        for x in keys[1:]:
            xor ^= x
        dense.append(xor)

    solution = ""
    for d in dense:
        solution += f'{d:02x}'

    return solution


def neighbours(point):

    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        yield point[0] + dx, point[1] + dy


def solve(key):

    grid = defaultdict(int)

    for i in range(128):
        full_key = f"{key}-{i}"
        hash = knot_hash(full_key)

        y = 0
        for h in hash:
            bh = f'{int(h, 16):0>4b}'
            for b in bh:
                grid[(i, y)] = int(b)
                y += 1

    # grid flow
    solution = 0
    for x, y in product(range(128), repeat=2):
        if grid[(x, y)] == 1:
            solution += 1

            expand = [(x, y)]

            while expand:
                state = expand.pop()
                grid[state] = -1

                for point in neighbours(state):
                    if grid[point] == 1:
                        expand.append(point)

    return solution


def main():

    with open('input') as in_f:
        data = in_f.readline().strip()

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
