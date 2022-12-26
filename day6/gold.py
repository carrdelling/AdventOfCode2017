

def solve(data):

    seen = set()
    when = {}
    current = (0,)
    n = len(data)

    cycles = 0

    while current not in seen:
        seen.add(current)
        when[current] = cycles

        pointer = None
        max_v = 0
        for idx in range(n):

            if data[idx] > max_v:
                max_v = data[idx]
                pointer = idx

        charges = data[pointer]
        data[pointer] = 0

        full_charges = charges // n
        charges = charges % 16

        for idx in range(n):
            data[idx] += full_charges

        while charges > 0:

            pointer = pointer + 1 if pointer < 15 else 0
            data[pointer] += 1
            charges -= 1

        current = tuple(data)
        cycles += 1

    return cycles - when[current]


def main():

    with open('input') as in_f:
        data = list(map(int, in_f.readline().strip().split()))

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
