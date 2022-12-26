from collections import defaultdict, deque
from string import ascii_letters


def apply_op(program, pc, register, queue):

    instruction = program[pc]
    ins, *params = instruction
    to_send = None
    blocked = False

    # parse params
    if len(params) == 2:
        if params[1] in ascii_letters:
            params[1] = register[params[1]]
        else:
            params[1] = int(params[1])

    # regular ops
    if ins == 'set':
        register[params[0]] = params[1]
        pc += 1

    if ins == 'add':
        register[params[0]] += params[1]
        pc += 1

    if ins == 'mul':
        register[params[0]] *= params[1]
        pc += 1

    if ins == 'mod':
        register[params[0]] = register[params[0]] % params[1]
        pc += 1

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

    # send
    if ins == 'snd':
        to_send = register[params[0]]
        pc += 1

    # receive
    if ins == 'rcv':
        if len(queue) > 0:
            register[params[0]] = queue.popleft()
            pc += 1
        else:
            blocked = True

    return pc, register, queue, to_send, blocked


def solve(program):

    register_a = defaultdict(int)
    register_b = defaultdict(int)
    register_a['p'] = 0
    register_b['p'] = 1

    queue_a = deque([])
    queue_b = deque([])
    pc_a = 0
    pc_b = 0

    sent_by_b = 0

    a_runs = True
    b_runs = True

    while a_runs or b_runs:

        # a first
        a_runs = False

        while -1 < pc_a < len(program):

            output = apply_op(program, pc_a, register_a, queue_a)
            pc_a, register_a, queue_a, to_send, blocked = output

            if blocked:
                break
            a_runs = True

            if to_send is not None:
                queue_b.append(to_send)

        # then b
        b_runs = False
        while -1 < pc_b < len(program):
            output = apply_op(program, pc_b, register_b, queue_b)
            pc_b, register_b, queue_b, to_send, blocked = output

            if blocked:
                break
            b_runs = True

            if to_send is not None:
                sent_by_b += 1
                queue_a.append(to_send)

    # both process have finished
    solution = sent_by_b

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
