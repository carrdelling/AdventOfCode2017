
def solve(a, b):

    factor_a = 16807
    factor_b = 48271
    modulo = 2147483647
    test_modulo = 2 ** 16

    N_OPS = 40000000
    equal = 0
    for idx in range(N_OPS):
        a = (a * factor_a) % modulo
        b = (b * factor_b) % modulo

        a_bin = a % test_modulo
        b_bin = b % test_modulo

        equal += 1 if a_bin == b_bin else 0

    solution = equal

    return solution


def main():

    with open('input') as in_f:
        a = int(in_f.readline().strip().split(' ')[-1])
        b = int(in_f.readline().strip().split(' ')[-1])

    solution = solve(a, b)

    print(solution)


if __name__ == "__main__":

    main()
