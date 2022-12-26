from collections import Counter


def solve(data):

    directions = {
        'n': [-2, 0],
        's': [2, 0],
        'nw': [-1, -1],
        'sw': [1, -1],
        'ne': [-1, 1],
        'se': [1, 1],
    }

    steps = Counter(data)

    x = sum(directions[k][0] * v for k, v in steps.items())
    y = sum(directions[k][1] * v for k, v in steps.items())

    d = abs(y) + ((abs(x) - abs(y)) // 2)

    return d


def main():

    with open('input') as in_f:
        data = in_f.readline().strip().split(',')

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
