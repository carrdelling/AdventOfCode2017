

def solve(step):

    buffer = [0]
    idx = 0

    for s in range(1, 2018):
        idx = (idx + step) % len(buffer)
        buffer = buffer[:idx] + [s] + buffer[idx:]
        idx = (idx + 1) % len(buffer)

    solution = buffer[idx % len(buffer)]

    return solution


def main():

    with open('input') as in_f:
        step = int(in_f.readline().strip())

    solution = solve(step)

    print(solution)


if __name__ == "__main__":

    main()
