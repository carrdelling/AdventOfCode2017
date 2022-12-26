

def solve(data):

    solution = sum([max(row) - min(row) for row in data])

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
