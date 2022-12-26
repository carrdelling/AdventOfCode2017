

def solve(data):

    reachable = {'0'}
    visited = set()

    active = reachable - visited

    while active:

        for a in active:
            visited.add(a)
            for s in data[a]:
                reachable.add(s)

        active = reachable - visited

    return len(reachable)


def main():

    pipes = {}
    with open('input') as in_f:
        for row in in_f:

            pre, post = row.strip().split(' <-> ')
            post = post.split(', ')
            pipes[pre] = post

    solution = solve(pipes)

    print(solution)


if __name__ == "__main__":

    main()
