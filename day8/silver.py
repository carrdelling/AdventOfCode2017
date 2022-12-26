from collections import defaultdict


def guard(v, cond, gv):

    if cond == '==':
        return v == gv
    if cond == '!=':
        return v != gv
    if cond == '>':
        return v > gv
    if cond == '>=':
        return v >= gv
    if cond == '<':
        return v < gv
    if cond == '<=':
        return v <= gv

    assert False


def solve(data):

    memory = defaultdict(int)

    for reg, op, v, chk, cond, cv in data:

        # do we run the instruction?
        pre = memory[chk]

        if not guard(pre, cond, cv):
            continue

        if op == 'inc':
            memory[reg] += v

        if op == 'dec':
            memory[reg] -= v

    solution = max(memory.values())

    return solution


def main():

    data = []
    with open('input') as in_f:
        for row in in_f:
            reg, op, v, _, chk, cond, cv = row.strip().split()
            v = int(v)
            cv = int(cv)

            data.append((reg, op, v, chk, cond, cv))

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
