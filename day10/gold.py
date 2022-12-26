

def encrypt(keys, data, current=0, skip=0):

    size = len(data)

    for k in keys:

        subchain = [data[(current+ii) % size] for ii in range(k)][::-1]
        for ii in range(k):
            idx = (current+ii) % size
            data[idx] = subchain[ii]

        # move current
        current += k + skip
        current = current if current < size else current - size

        # increase skip
        skip += 1

    return data, current, skip


def solve(data):

    ascii = [ord(x) for x in data]
    keys = ascii + [17, 31, 73, 47, 23]

    data = list(range(256))
    data, current, skip = encrypt(keys, data)

    for r in range(63):

        data, current, skip = encrypt(keys, data, current, skip)

    dense = []
    for offset in range(16):
        keys = data[16*offset:(16*offset) + 16]

        xor = keys[0]
        for x in keys[1:]:
            xor ^= x
        dense.append(xor)

    solution = ""
    for d in dense:
        solution += f'{d:02x}'

    return solution


def main():

    with open('input') as in_f:
        data = list(in_f.readline().strip())

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
