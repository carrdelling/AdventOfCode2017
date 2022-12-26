from collections import defaultdict
from string import ascii_letters


def solve(program):

    register = defaultdict(int)
    pc = 0
    mul_times = 0

    while -1 < pc < len(program):
        instruction = program[pc]
        ins, *params = instruction

        # parse params
        if len(params) == 2:
            if params[1] in ascii_letters:
                params[1] = register[params[1]]
            else:
                params[1] = int(params[1])

        # ops
        if ins == 'set':
            register[params[0]] = params[1]
            pc += 1
            continue
        if ins == 'sub':
            register[params[0]] -= params[1]
            pc += 1
            continue
        if ins == 'mul':
            mul_times += 1
            register[params[0]] *= params[1]
            pc += 1
            continue
        if ins == 'jnz':
            if params[0] in ascii_letters:
                if register[params[0]] != 0:
                    pc += params[1]
                else:
                    pc += 1
            elif int(params[0]) != 0:
                pc += params[1]
            else:
                pc += 1
            continue

    solution = mul_times

    return solution


def main():

    data = []
    with open('input') as in_f:
        for row in in_f:
            ins = row.strip().split()
            data.append(ins)

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
