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

    flagged_turn = {
        'U': 'D',
        'D': 'U',
        'L': 'R',
        'R': 'L'
    }

    current = (max_x // 2, max_y // 2)
    direction = 'U'
    BURSTS = 10000000
    infections = 0

    for _ in range(BURSTS):

        infested = data[current] == '#'
        clean = data[current] == '.'
        weakened = data[current] == 'W'
        flagged = data[current] == 'F'

        if infested:
            direction = infected_turn[direction]
        if clean:
            direction = clean_turn[direction]
        if flagged:
            direction = flagged_turn[direction]
        if weakened:
            pass

        infections += 1 if weakened else 0

        if infested:
            data[current] = 'F'
        if clean:
            data[current] = 'W'
        if flagged:
            data[current] = '.'
        if weakened:
            data[current] = '#'

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
