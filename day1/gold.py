

def solve(data):

    dup = data + data
    n = len(data) // 2
    solution = 0
    for a, b in zip(data, dup[n:]):
        if a == b:
            solution += a

    return solution


def main():

    with open('input') as in_f:
        data = [int(c) for c in in_f.readline().strip()]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
