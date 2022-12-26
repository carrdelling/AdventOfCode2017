

def get_group(start, pipes):

    reachable = {start}
    visited = set()

    active = reachable - visited

    while active:

        for a in active:
            visited.add(a)
            for s in pipes[a]:
                reachable.add(s)

        active = reachable - visited

    return reachable


def solve(data):

    groups = 0

    targets = set(data)

    while targets:

        root = next(iter(targets))

        group = get_group(root, data)
        targets -= group

        groups += 1

    return groups


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
