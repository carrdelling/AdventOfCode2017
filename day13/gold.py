from functools import lru_cache


@lru_cache
def is_scanner(height, time):
    offset = time % ((height - 1) * 2)
    pos = 2 * (height - 1) - offset if offset > height - 1 else offset

    return pos == 0


def solve(data):

    delay = 0

    while True:

        for pos, depth in data.items():
            if is_scanner(depth, delay + pos):
                break
        else:
            return delay

        delay += 1


def main():

    layers = {}
    with open('input') as in_f:
        for row in in_f:
            layer, dist = row.strip().split(': ')
            layers[int(layer)] = int(dist)

    solution = solve(layers)

    print(solution)


if __name__ == "__main__":

    main()
