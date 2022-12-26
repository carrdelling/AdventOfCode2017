

def solve(data):

    # find root
    childs = set()
    nodes = set()

    for parent, w, child in data:

        nodes.add(parent)

        for c in child:
            childs.add(c)

    root = list(nodes - childs)[0]

    return root


def main():

    data = []
    with open('input') as in_f:
        for row in in_f:
            chunks = row.strip().split(' -> ')

            childs = chunks[1].split(', ') if len(chunks) > 1 else []
            parent, w = chunks[0][:-1].split(' (')
            w = int(w)

            data.append((parent, w, childs))

    solution = solve(data)

    print(solution)


if __name__ == "__main__":

    main()