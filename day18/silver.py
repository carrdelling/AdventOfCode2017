from collections import defaultdict
from string import ascii_letters


def solve(program):

    register = defaultdict(int)
    sounds_played = []
    sounds_recovered = []
    pc = 0

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
        if ins == 'snd':
            sounds_played.append(register[params[0]])
            pc += 1
            continue
        if ins == 'add':
            register[params[0]] += params[1]
            pc += 1
            continue
        if ins == 'mul':
            register[params[0]] *= params[1]
            pc += 1
            continue
        if ins == 'mod':
            register[params[0]] = register[params[0]] % params[1]
            pc += 1
            continue
        if ins == 'jgz':
            if params[0] in ascii_letters:
                if register[params[0]] > 0:
                    pc += params[1]
                else:
                    pc += 1
            elif int(params[0]) > 0:
                pc += params[1]
            else:
                pc += 1
            continue
        if ins == 'rcv':
            if register[params[0]] > 0:
                sounds_recovered.append(sounds_played[-1])
                pc = len(program)
            pc += 1
            continue

    solution = sounds_recovered[0]

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
