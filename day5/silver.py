

def solve(data):

    current = 0
    steps = 0

    while -1 < current < len(data):
        steps += 1
        old = current
        current += data[current]
        data[old] += 1

    return steps


def main():

    data = []
    with open('input') as in_f:
        for row in in_f:
            data.append(int(row.strip()))

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
