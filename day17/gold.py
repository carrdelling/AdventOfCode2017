from collections import deque


def solve(step):

    spinlock = deque([0])

    for i in range(1, 50000001):
        spinlock.rotate(-step)
        spinlock.append(i)

        if i % 1000000 == 0:
            print(i)

    solution = spinlock[spinlock.index(0) + 1]

    return solution


def main():

    with open('input') as in_f:
        step = int(in_f.readline().strip())

    solution = solve(step)

    print(solution)


if __name__ == "__main__":

    main()
