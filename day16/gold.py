
def solve(data):

    dance = [chr(i) for i in range(97, 113)]
    bis = 1000000000
    current = 0
    solution = ''

    seen = {}
    while current < bis:

        dance = one_dance(dance, data)

        if tuple(dance) in seen.values():
            solution = ''.join(seen[1000000000 % len(seen)])
            break

        current += 1
        seen[current] = tuple(dance)

    return solution


def one_dance(dance, data):

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

    return dance


def main():

    with open('input') as in_f:
        data = in_f.readline().strip().split(',')

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
