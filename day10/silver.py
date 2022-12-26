

def solve(data):

    numbers = list(range(256))
    size = len(numbers)
    skip = 0
    current = 0

    for n in data:

        subchain = [numbers[(current+ii) % size] for ii in range(n)][::-1]
        for ii in range(n):
            idx = (current+ii) % size
            numbers[idx] = subchain[ii]

        # move current
        current += n + skip
        current = current if current < size else current - size

        # increase skip
        skip += 1

    solution = numbers[0] * numbers[1]

    return solution


def main():

    with open('input') as in_f:
        data = list(map(int, in_f.readline().strip().split(',')))

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
