

def distance(x, y):

    xx, yy = abs(x), abs(y)

    xx = max(0, xx - yy)

    return yy + (xx // 2)


def solve(data):

    directions = {
        'n': [-2, 0],
        's': [2, 0],
        'nw': [-1, -1],
        'sw': [1, -1],
        'ne': [-1, 1],
        'se': [1, 1],
    }

    current = [0, 0]
    max_distance = 0

    for s in data:

        current = [current[0] + directions[s][0], current[1] + directions[s][1]]
        max_distance = max(max_distance, distance(*current))

    return max_distance


def main():

    with open('input') as in_f:
        data = in_f.readline().strip().split(',')

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
