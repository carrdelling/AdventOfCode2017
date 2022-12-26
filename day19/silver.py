from collections import defaultdict
from string import ascii_letters


def forward(pos, direction):

    delta = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }

    return pos[0] + delta[direction][0], pos[1] + delta[direction][1]


def shift(pos, direction, data):

    deltas = {
        'U': [(0, -1, 'L', '-'), (0, 1, 'R', '-')],
        'D': [(0, -1, 'L', '-'), (0, 1, 'R', '-')],
        'L': [(-1, 0, 'U', '|'), (1, 0, 'D', '|')],
        'R': [(-1, 0, 'U', '|'), (1, 0, 'D', '|')]
    }

    for dx, dy, dir_, valid in deltas[direction]:
        next_pos = pos[0] + dx, pos[1] + dy

        if data[next_pos] == valid:
            return next_pos, dir_


def solve(data):

    start_y = list({p[1]: v for p, v in data.items() if p[0] == 0 and v == '|'})[0]

    current = (0, start_y)
    direction = 'D'

    message = []

    while data[current] != ' ':

        while data[current] != '+':
            current = forward(current, direction)
            if data[current] in ascii_letters:
                message.append(data[current])
                if data[current] == 'T':
                    break

        if data[current] == 'T':
            break

        current, direction = shift(current, direction, data)
        if data[current] in ascii_letters:
            message.append(data[current])
            if data[current] == 'T':
                break

    solution = ''.join(message)

    return solution


def main():

    data = defaultdict(lambda: ' ')
    with open('input') as in_f:
        for x, row in enumerate(in_f):
            for y, c in enumerate(row.rstrip()):
                data[(x, y)] = c

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
