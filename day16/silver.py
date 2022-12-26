
def solve(data):

    dance = [chr(i) for i in range(97, 113)]

    for ins in data:
        if ins[0] == 's':
            chop = int(ins[1:])

            before = dance[-chop:]
            after = dance[:-chop]
            dance = before + after
            continue

        if ins[0] == 'x':
            first, second = map(int, ins[1:].split('/'))
            dance[second], dance[first] = dance[first], dance[second]
            continue

        if ins[0] == 'p':
            first, second = ins[1:].split('/')
            idx_1 = dance.index(first)
            idx_2 = dance.index(second)
            dance[idx_2], dance[idx_1] = dance[idx_1], dance[idx_2]
            continue

    solution = ''.join(dance)

    return solution


def main():

    with open('input') as in_f:
        data = in_f.readline().strip().split(',')

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
