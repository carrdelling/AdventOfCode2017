from collections import defaultdict


def forward(pos, direction):

    delta = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }

    return pos[0] + delta[direction][0], pos[1] + delta[direction][1]


def solve(data):

    max_x = max(x[0] for x in data)
    max_y = max(x[1] for x in data)

    infected_turn = {
        'U': 'R',
        'D': 'L',
        'L': 'U',
        'R': 'D'
    }

    clean_turn = {
        'U': 'L',
        'D': 'R',
        'L': 'D',
        'R': 'U'
    }

    current = (max_x // 2, max_y // 2)
    direction = 'U'
    BURSTS = 10000
    infections = 0

    for _ in range(BURSTS):

        infested = data[current] == '#'

        direction = infected_turn[direction] if infested else clean_turn[direction]
        infections += 0 if infested else 1
        data[current] = '.' if infested else '#'
        current = forward(current, direction)

    solution = infections

    return solution


def main():

    data = defaultdict(lambda: '.')
    with open('input') as in_f:
        for x, row in enumerate(in_f):
            for y, c in enumerate(row.rstrip()):
                data[(x, y)] = c

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
