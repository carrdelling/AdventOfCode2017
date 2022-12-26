from collections import deque, defaultdict


def solve(start, cycles, states):

    tape = defaultdict(int)
    cursor = 0

    current = start

    for _ in range(cycles):
        c_val = tape[cursor]
        key = (current, c_val)

        write, move, next_state = states[key]

        tape[cursor] = write
        cursor += 1 if move == 'right' else -1
        current = next_state

    checksum = sum(tape.values())

    solution = checksum

    return solution


def main():

    states = {}
    with open('input') as in_f:
        start = in_f.readline().strip().split(' ')[-1][0]
        steps = int(in_f.readline().strip().split(' ')[-2])

        lines = deque(in_f.readlines())

        while lines:
            lines.popleft()
            state = lines.popleft().strip()[:-1].split(' ')[-1]
            lines.popleft()
            write = int(lines.popleft().strip()[:-1].split(' ')[-1])
            move = lines.popleft().strip()[:-1].split(' ')[-1]
            next_state = lines.popleft().strip()[:-1].split(' ')[-1]

            states[(state, 0)] = (write, move, next_state)
            lines.popleft()
            write = int(lines.popleft().strip()[:-1].split(' ')[-1])
            move = lines.popleft().strip()[:-1].split(' ')[-1]
            next_state = lines.popleft().strip()[:-1].split(' ')[-1]

            states[(state, 1)] = (write, move, next_state)

    solution = solve(start, steps, states)

    print(solution)


if __name__ == "__main__":

    main()
