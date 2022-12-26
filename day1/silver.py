

def solve(data):

    solution = 0
    for a, b in zip(data, data[1:]):
        if a == b:
            solution += a
    else:
        if data[0] == data[-1]:
            solution += data[0]

    return solution


def main():

    with open('input') as in_f:
        data = [int(c) for c in in_f.readline().strip()]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
