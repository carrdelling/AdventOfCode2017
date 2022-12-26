

def solve(stream):

    stack = 0
    score = 0

    garbage = False

    while len(stream) > 0:

        c = stream.pop()

        if c == '{' and not garbage:
            stack += 1
        if c == '}' and not garbage:
            score += stack
            stack -= 1

        if c == '<':
            garbage = True

        if c == '>' and garbage:
            garbage = False

        if c == '!' and garbage:
            stream.pop()

    return score


def main():

    with open('input') as in_f:
        data = list(in_f.readline().strip())[::-1]

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()
