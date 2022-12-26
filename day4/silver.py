

def solve(data):

    valid = sum([1 if len(row) == len(set(row)) else 0 for row in data])

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
