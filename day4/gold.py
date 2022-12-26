
def solve(data):

    valid = 0

    for row in data:
        vocab = {tuple(sorted(v)) for v in row}

        if len(row) == len(vocab):
            valid += 1

    return valid


def main():

    data = []
    with open('input') as in_f:
        for row in in_f:
            data.append(row.strip().split())

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
