from itertools import product


def solve(data):

    solution = 0
    for row in data:
        for a, b in product(row, repeat=2):
            if a % b == 0 and a != b:
                solution += a // b

    return solution


def main():

    data = []
    with open('input') as in_f:
        for row in in_f:
            data.append(tuple(map(int, row.strip().split())))

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
