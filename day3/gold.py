from collections import defaultdict


def neighbours(x, y):

    for _x, _y in [(-1, -1), (-1, 0),(-1, 1),
                   (0, -1), (0, 1),
                   (1, -1), (1, 0),(1, 1)]:
        yield x + _x, y + _y


def score(x, y, matrix):

    return sum([matrix[(_x, _y)] for _x, _y in neighbours(x, y)])


def solve(data):

    # build the matrix this time
    matrix = defaultdict(int)
    current = (0, 0)
    matrix[current] = 1
    inc = 1
    solution = None

    while solution is None:

        # go right
        for i in range(inc):
            current = current[0], current[1] + 1
            matrix[current] = score(current[0], current[1], matrix)

            if solution is None and matrix[current] > data:
                solution = matrix[current]

        # go up
        for i in range(inc):
            current = current[0] - 1, current[1]
            matrix[current] = score(current[0], current[1], matrix)

            if solution is None and matrix[current] > data:
                solution = matrix[current]

        inc += 1

        # go left
        for i in range(inc):
            current = current[0], current[1] - 1
            matrix[current] = score(current[0], current[1], matrix)

            if solution is None and matrix[current] > data:
                solution = matrix[current]

        # go down
        for i in range(inc):
            current = current[0] + 1, current[1]
            matrix[current] = score(current[0], current[1], matrix)

            if solution is None and matrix[current] > data:
                solution = matrix[current]

        inc += 1

    return solution


def main():

    with open('input') as in_f:
        data = int(in_f.readline().strip())

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
